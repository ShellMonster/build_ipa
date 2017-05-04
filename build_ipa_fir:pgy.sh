#!/bin/sh
#0406测试mac打包
#for_道长（Q_1013373636）

osascript -e 'display notification "开始执行脚本" with title "打包窗口输出"'

osascript -e 'display notification "切换执行路径" with title "打包窗口输出"'

#此处请修改项目目录
cd ~/Desktop/kzd-ios/

#此区域请修改对应名称及目录
scheme="xxxx"
archiveName="${scheme}"
workspaceName="kzd.xcworkspace"
configuration="Release"
archivePath="/Users/mac/Desktop/${archiveName}$(date +%Y年%m月%d日%H/%M)"
archivefile="/Users/mac/Desktop/${archiveName}$(date +%Y年%m月%d日%H/%M).xcarchive"
#请注意对应release_exportOptions.plis文件路径
exportOptionsPlist="/Users/mac/Desktop/release_exportOptions.plist"
team_id="xxxxxxxxxxxxx"
ipaPath="/Users/mac/Desktop/${archiveName}$(date +%Y年%m月%d日%H/%M)"
ipafile="/Users/mac/Desktop/${archiveName}$(date +%Y年%m月%d日%H/%M)"
#mobileprovision_uuid="xxxxxxxxxxxxxxxxxxxxx"
#蒲公英key
uKey="xxxxxxxxxxxxx"
api_key="xxxxxxxxxxxxx"



#清理xcodebuild缓存
osascript -e 'display notification "清理xcodebuild缓存" with title "打包窗口输出"'
xcodebuild clean

osascript -e 'display notification "开始编译" with title "打包窗口输出"'

xcodebuild archive -workspace "$workspaceName" -scheme "$scheme" -configuration "$configuration" -archivePath "$archivePath" #CODE_SIGN_IDENTITY=${CODE_SIGN_IDENTITY} PROVISIONING_PROFILE=${mobileprovision_uuid} #CONFIGURATION_BUILD_DIR="$configurationBuildDir" CODE_SIGN_IDENTITY="$codeSignIdentity" PROVISIONING_PROFILE="$provisioningProfile" >> $log_path

osascript -e 'display notification "输出编译路径" with title "打包窗口输出"'
#osascript -e 'display notification "${archivefile}" with title "打包窗口输出"'
osascript -e 'display notification "编译完成，判断是否成功" with title "打包窗口输出"'

# -s 参数判断 ipa包 
if [ -s "${archivefile}" ]; then
	osascript -e 'display notification "编译成功" with title "打包窗口输出"'
	osascript -e 'display notification "开始导出" with title "打包窗口输出"'
	osascript -e 'display notification "开始修改plist签名" with title "打包窗口输出"'
		sed -i "" "/>teamID</{n;s/>[^<>]*</>${team_id}</;}" ${exportOptionsPlist}
    	xcodebuild -exportArchive -archivePath "$archivefile" -exportOptionsPlist "$exportOptionsPlist" -exportPath "$ipaPath" #>> $log_path
    		if [ -s "${ipafile}" ]; then
    			osascript -e 'display notification "导出成功" with title "打包窗口输出"'
    			else osascript -e 'display notification "导出失败" with title "打包窗口输出"'
    		fi
	else
	osascript -e 'display notification "编译失败" with title "打包窗口输出"'
fi

#上传ipa至fir(第一条为Api登录授权)
#fir login XXX_YOUR_API_TOKEN_XXX
#fir publish -c "first version log" -s ${scheme} ${ipafile}/${scheme}.ipa

#检测最优上传ip
#sh -c "$(curl -sSL https://gist.githubusercontent.com/trawor/5dda140dee86836b8e60/raw/turbo-qiniu.sh)"

#上传ipa至蒲公英
curl -F "file=@${ipafile}/${scheme}.ipa" -F "uKey=${uKey}" -F "_api_key=${api_key}" https://qiniu-storage.pgyer.com/apiv1/app/upload
#Api帮助文档地址
#https://www.pgyer.com/doc/api#uploadApp

# build_ipa
build_ipa-fir/pgy </br>

**本教程主要针对xcode编译打包功能，依赖xcode自带工具包。** </br>
原文链接[http://www.asoheikeji.com/index.php/2017/05/04/build-ipa-fir/] </br>
#### 请在运行脚本前检查是否已安装xcode工具！
```
xcode-select --install
```

**请在xcode内配置icon等各项，保证xcode能正常archive；**

#### 运行命令------
```
#请自行修改sh后跟的文件路径及文件名！
sh ~/Desktop/build_ipa_fir.sh
```

### 运行截图------
<img src="/1.jpeg" alt="1" height="300" width="600" > </br>
### 打包及导出成功截图------
<img src="/2.jpeg" alt="2" height="300" width="800" > </br>

*上传成功后终端会反馈回执！
fir反馈内容为包下载链接！
蒲公英反馈内容为json格式内容！*

以下为执行脚本命令，已添加注释内容！
```
#!/bin/sh
#0406测试mac打包
#for_道长（Q_1013373636）

osascript -e 'display notification "开始执行脚本" with title "打包窗口输出"'

osascript -e 'display notification "切换执行路径" with title "打包窗口输出"'

#此处请修改项目目录
cd ~/Desktop/kzd-ios/

#此区域请修改对应名称及目录
scheme="kkz"
archiveName="${scheme}"
workspaceName="kkz.xcworkspace"
configuration="Release"
archivePath="/Users/mac/Desktop/${archiveName}$(date +%Y年%m月%d日%H:%M)"
archivefile="/Users/mac/Desktop/${archiveName}$(date +%Y年%m月%d日%H:%M).xcarchive"
#请注意对应release_exportOptions.plis文件路径
exportOptionsPlist="/Users/mac/Desktop/release_exportOptions.plist"
team_id="xxxxxxxx"#可查看钥匙串内容，查找Dist证书获取team_id。
ipaPath="/Users/mac/Desktop/${archiveName}$(date +%Y年%m月%d日%H:%M)"
ipafile="/Users/mac/Desktop/${archiveName}$(date +%Y年%m月%d日%H:%M)"
#mobileprovision_uuid="xxxxxxxxx"
#蒲公英key
uKey="xxxxxxxxxxxxxxxx"
api_key="xxxxxxxxxxxxxxxxxx"

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
```

**以上代码，可复制后保存文本为.sh格式脚本文件便于执行；也可以使用vi命令保存！**

*附：笔者非专业开发人士，编写代码主要为提高工作效率及偷懒，所以遇到代码排版及bug问题可随时反馈至留言处，便于及时改正！*
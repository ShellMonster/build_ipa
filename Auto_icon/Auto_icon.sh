#!/bin/sh
#0505自动裁剪导入logo
#for_道长（Q_1013373636）


#裁剪logo文件路径
filename="/Users/mac/Downloads/贷款王2.png"
dirname="/Users/mac/Desktop/kzd-ios/kzd/Assets.xcassets/AppIcon_DKW.appiconset/"

##############此处为logo大小配置，目前已设置满足xcode打包需求，如无其他需要请勿修改##############
name_array=("Icon-20×20@2x-1.png" "Icon-20×20@3×.png" "Icon-29×29@1×-1.png" "Icon-29×29@2x-2.png" "Icon-29×29@3×-1.png" "Icon-40×40@2×-1.png" "Icon-40×40@3×.png" "Icon-57×57@1x.png" "Icon-57×57@2x.png" "Icon-60×60@2×-1.png" "Icon-60×60@3×.png")
size_array=("40" "60" "29" "58" "87" "80" "120" "57" "114" "120" "180")
mkdir $dirname
for ((i=0;i<${#name_array[@]};++i)); do
    m_dir=$dirname/${name_array[i]}
    cp $filename $m_dir
    sips -Z ${size_array[i]} $m_dir
done
##############此处为logo大小配置，目前已设置满足xcode打包需求，如无其他需要请勿修改##############


#添加logo自动排序，此处请修改好Contents.json文件路径
cp ~/Desktop/build_shell/Contents.json ${dirname}
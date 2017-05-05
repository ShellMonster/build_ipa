#### 如何利用shell脚本自动裁剪icon并导入xcode。 </br>
- [-] **功能：**
- [-] 1，自动裁剪logo，按对应尺寸；
- [-] 2，自动导入xcode路径（需配置项目路径）；
- [-] 3，自动排序logo，适配iOS各项设备；
</br>
##### 执行请打开终端输入---
```
sh ~/Desktop/Auto_icon.sh
```

##### 执行时可看到导入时终端输出---  </br>
<img src="/source/auto_icon.png" alt="如何利用shell脚本自动裁剪icon并导入xcode" >

##### 完整代码如下，如需下载请点击后续链接跳转至git。
```
#裁剪logo文件路径
filename="/Users/mac/Downloads/小情绪.png"
dirname="/Users/mac/Desktop/my_projuct_oc/Relax/Assets.xcassets/AppIcon.appiconset/"

name_array=("Icon-20×20@2x-1.png" "Icon-20×20@3×.png" "Icon-29×29@1×-1.png" "Icon-29×29@2x-2.png" "Icon-29×29@3×-1.png" "Icon-40×40@2×-1.png" "Icon-40×40@3×.png" "Icon-57×57@1x.png" "Icon-57×57@2x.png" "Icon-60×60@2×-1.png" "Icon-60×60@3×.png")
size_array=("40" "60" "29" "58" "87" "80" "120" "57" "114" "120" "180")
mkdir $dirname
for ((i=0;i<${#name_array[@]};++i)); do
    m_dir=$dirname/${name_array[i]}
    cp $filename $m_dir
    sips -Z ${size_array[i]} $m_dir
done

#添加logo自动排序
cp ~/Desktop/build_shell/Contents.json ${dirname}
```

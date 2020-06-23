#批量抠图代码
from removebg import RemoveBg
import os
rmbg=RemoveBg('yGvc1A92w5wszi6j1oW11S9S',"error.log")
path='%s/pictures'%os.getcwd() #图片放到程序的同级文件夹pictures里面
#需要再在python的目录下面建一个文件夹pictures(当然可以自己命名，但是要记得替换上一层代码的名称)
#然后把需要抠的图片放进去即可，比如我的项目目录是C:\Documents\Python Projects\pictures
for pic in os.listdir(path):    
    rmbg.remove_background_from_img_file("%s\%s"%(path,pic))
#其他直接copy就可以咯！

# -*- coding: utf-8 -*
from PIL import Image

x=503 #图片尺寸
y=122

im=Image.new("RGB",(x,y))
file=open('a.txt')

for i in range(0,x):
        for j in range(0,y):
                line=file.readline()
                rgb=line.split(",") #将混杂在文本中的逗号去除
                im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))

im.show()

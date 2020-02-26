# -*- coding: utf-8 -*

from PIL import Image

x=29
y=29

im=Image.new("RGB",(x,y))
white = (255, 255, 255)
black = (0, 0, 0)
file=open('qrcode.txt')

for i in range(x):
        f = file.readline()
        for j in range(y):
                if f[j] == '1':
                        im.putpixel((j, i), black)
                else:
                        im.putpixel((j, i), white)
#im.show()
im.save("1.png")
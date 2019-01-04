# -*- coding:utf-8 -*-

import os.path
import sys
from PIL import Image, ImageDraw, ImageFont, ImageColor

def add_num(img, font, num, outimg):
    myimage = Image.open(img)
    myfont = ImageFont.truetype(font=font, size=40)
    fontcolor = ImageColor.colormap.get('red')
    draw = ImageDraw.Draw(myimage)
    width, height = myimage.size
    draw.text((width-30, 0), str(num), font=myfont, fill=fontcolor)
    myimage.save(outimg)
    

if __name__ == '__main__':
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    imgname = dirname + os.sep + 'image' + os.sep + 'src.jpg'
    fontname = dirname + os.sep + 'font' + os.sep + 'arial.ttf'
    outimg = dirname + os.sep + 'outimg.jpg'
    add_num(imgname, fontname, 1, outimg)

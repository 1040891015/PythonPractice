# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageColor
import os.path
import sys
import re
import time


def search_img(path):
    '''查询指定路径下所有图片文件，并返回其绝对路径'''
    img_list = []
    img_type = ['img', 'jpg', 'bmp', 'png', 'gif']
    for root, dirs, files in os.walk(path):
        for name in files:
            file_name, file_type = os.path.splitext(name)
            if file_type[1:].lower() in img_type: #获取符合格式的所有文件
                img_path = os.path.join(root, name) #获取文件的绝对路径
                img_list.append(img_path)
    return img_list

def resize_img(img_in, img_out, w, h):
    '''等比缩放图片到指定宽高（不小于该尺寸）'''
    img = Image.open(img_in)
    x, y = img.size
    if w/h < x/y: #获取缩小比例
        ratio = y/h
    else:
        ratio = x/w
    x1 = int(x/ratio)
    y1 = int(y/ratio)
    img = img.resize((x1, y1), Image.ANTIALIAS)
    box = ((x1-w)/2, (y1-h)/2, (x1+w)/2, (y1+h)/2) # 图片中央w*h的区域
    region = img.crop(box) # 按区域裁剪图片
    region.save(img_out)

def add_point(img_in, img_out, num):
    '''在图片右上角加消息通知（先缩小再添加）'''
    img_head = Image.open(img_in)
    x, y = img_head.size
    r = int(x/6) # 根据图像大小确定消息通知圆点的半径
    img = Image.new(mode='RGBA', size=(x,y))
    img_head = img_head.resize((x-2*r,y-2*r), Image.ANTIALIAS)
    img.paste(img_head,(r,r)) # 将缩小的图像粘贴在原尺寸画布上
    img_point = Image.new(mode='RGBA', size=(2*r,2*r)) # 创建圆点画布
    draw_point = ImageDraw.Draw(img_point)
    draw_point.ellipse((0,0,2*r,2*r), fill='red', outline='red') # 画一个红色圆点，半径为r
    fontsize = int(1.5*r) # 设置字体
    fontcolor = ImageColor.colormap.get('white')
    fonttype = ImageFont.truetype(font='C:\\Windows\\Fonts\\arial.ttf', size=fontsize)
    fontpos = (int(r-len(str(num))*fontsize/4), int(r-fontsize/2)) # 确定数字在圆点坐标（按数字像素宽高比为1:2）
    draw_point.text(fontpos, str(num), font=fonttype, fill=fontcolor) # 将数字写入图片  
    R, G, B, A = img_point.split() # 对RGBA模式图片分离通道
    img.paste(img_point,(x-2*r,0),mask=A) # PIL粘贴RGBA模式的图片时，alpha通道要提取出来作为mask传入
    img.save(img_out)

def add_point_2(img_in, img_out, num):
    '''在图片右上角加消息通知（直接添加）'''
    img = Image.open(img_in)
    x, y = img.size
    r = int(x/6) # 根据图像大小确定消息通知圆点的半径
    img_point = Image.new(mode='RGBA', size=(2*r,2*r)) # 创建圆点画布
    draw_point = ImageDraw.Draw(img_point)
    draw_point.ellipse((0,0,2*r,2*r), fill='red', outline='red') # 画一个红色圆点，半径为r
    fontsize = int(1.5*r) # 设置字体
    fontcolor = ImageColor.colormap.get('white')
    fonttype = ImageFont.truetype(font='C:\\Windows\\Fonts\\arial.ttf', size=fontsize)
    fontpos = (int(r-len(str(num))*fontsize/4), int(r-fontsize/2)) # 确定数字在圆点坐标（按数字像素宽高比为1:2）
    draw_point.text(fontpos, str(num), font=fonttype, fill=fontcolor) # 将数字写入图片  
    R, G, B, A = img_point.split() # 对RGBA模式图片分离通道
    img.paste(img_point,(x-2*r,0),mask=A) # PIL粘贴RGBA模式的图片时，alpha通道要提取出来作为mask传入
    img.save(img_out)


if __name__ == '__main__':
    dirname, _ = os.path.split(os.path.abspath(sys.argv[0]))
    images_dir = dirname + os.sep + 'image'
    iphone_w = 320
    iphone_h = 568
    img_list = search_img(images_dir)
    for img in img_list:
        img_tmp = dirname + os.sep + 'image_new' + os.sep + \
                os.path.splitext(os.path.split(img)[1])[0] + '_' + str(int(time.time())) + os.path.splitext(os.path.split(img)[1])[1]
        resize_img(img, img_tmp, 640, 640)
        img_new = os.path.splitext(img_tmp)[0] + '_' + str(int(time.time())) + '.png'
        add_point_2(img_tmp, img_new, 1)
        os.remove(img_tmp)

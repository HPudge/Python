# !/user/bin/env/python 
# encoding:utf-8
# Author : mzyang
# @Date  : 2019/3/20


import os
import sys
import imagetotext
import time


# 调用图片转为txt的方法
def get_text(imagePath, txtPath):
    img_count = 1
    while img_count <= len(os.listdir(imagePath)):
        imageFile = imagePath + str(img_count) + '.png'
        txtFile = txtPath + str(img_count) + '.txt'
        imagetotext.image2txt(imageFile, txtFile)
        print('Loading: ' + str(img_count) + '%')
        img_count += 1


# 用命令行读取每个图片转化来的txt，设置时间间隔，形成动画效果
def run(txtPath):
    txt_count = 1
    while txt_count <= len(os.listdir(txtPath)):
        os.system('type ' + txtPath + str(txt_count) + '.txt')

        time.sleep(1.0/40)
        txt_count += 1
        os.system('cls')


if __name__ == '__main__':
    txt_path = r'E:\pytotal\MP4\txt' + '\\'
    img_path = r'E:\pytotal\MP4\images' + '\\'
    get_text(img_path, txt_path)
    run(txt_path)
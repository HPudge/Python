# !/user/bin/env/python 
# encoding:utf-8
# Author : mzyang
# @Date  : 2019/3/19

from PIL import Image
import numpy


'''
对每张png进行转化，图片的每一个像素与中间值127对比，每个点转为1或者空格。
'''


def image2txt(inputFile, outputFile):
    im = Image.open(inputFile).convert('L')
    charWidth = 100
    im = im.resize((charWidth, charWidth // 2))
    target_width, target_height = im.size
    data = numpy.array(im)[:target_height, :target_width]
    f = open(outputFile, 'w', encoding='utf-8')
    for row in data:
        for pixel in row:
            if pixel > 127:
                f.write('1')
            else:
                f.write(' ')
        f.write('\n')
    f.close()
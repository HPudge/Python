# !/user/bin/env/python 
# encoding:utf-8
# Author : mzyang
# @Date  : 2019/3/19

import os


# 利用ffmpeg将MP4格式的视频的帧抽取为PNG
def get_image(video_path, image_path):
    img_count = 1
    crop_time = 0.0
    while crop_time <= 12.0:
        os.system('ffmpeg -i %s -f image2 -ss %s -vframes 1 %s.png' % (video_path, str(crop_time), image_path + str(img_count)))
        img_count += 1
        print('Geting Image' + str(img_count) + '.png' + 'from time' + str(crop_time))
        crop_time += 0.1
    print('Image Collected')


if __name__ == '__main__':
    videoPath = 'E:/pytotal/MP4/1.MP4'
    imagePath = 'E:/pytotal/MP4/images/'
    get_image(videoPath, imagePath)

'''
将图片生成视频
'''
from cv2 import cv2 as cv
import numpy as np
import os
from PIL import Image
import time


def IntensityVideo(pic_dir, gesture, video_dir, fps, size):
    video_path = video_dir + gesture + '_' + str(fps) + '_' + '.avi'
    videowriter = cv.VideoWriter(
        video_path, cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size, 1)
    files = os.listdir(pic_dir)
    # f_len = len(files)
    # for i in range(1, 1561):
    #     file_path = pic_dir + 'Rock' + str(i) + '.jpg'
    #     print(file_path)
    #     try:
    #         img = cv.imread(file_path)
    #         videowriter.write(img)
    #     except:
    #         print("Error")
    #         continue
    #     # print('Waiting...')
    # for i in range(1, 1774):
    #     file_path = pic_dir + 'Scissor' + str(i) + '.jpg'
    #     print(file_path)
    #     try:
    #         img = cv.imread(file_path)
    #         videowriter.write(img)
    #     except:
    #         print("Error")
    #         continue
    #     # print('Waiting...')
    for i in range(1, 5250):
        file_path = pic_dir +  str(i) + '.png'
        print(file_path)
        try:
            img = cv.imread(file_path)
            videowriter.write(img)
        except:
            print("Error")
            continue
        # print('Waiting...')
    videowriter.release()

    # print('finished')
    num_pic = float(len(os.listdir(pic_dir)))
    video_duration = num_pic/fps
    print('The video duration time is %d seconds' % video_duration)


if __name__ == "__main__":
    Video_dir = 'Video'
    Pic_dir = '/mnt/d/temp/finish_project/yolo3-pytorch/img/'
    fps = 18

    # for files in os.listdir(Pic_dir):
    # pic_path = Pic_dir + files
    # name = os.path.splitext(files)[0]
    # IntensityVideo(pic_path,name,Video_dir,16,(768,640))

    name = 'final.avi'
    st = time.time()
    IntensityVideo(Pic_dir, name, Video_dir, fps, (768, 640))
    print('time: %d' % (time.time() - st))

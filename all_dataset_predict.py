#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
from yolo import YOLO
from PIL import Image
import time
import os
yolo = YOLO()

dir = '/mnt/d/temp/Celex_Tracking_data/photo/'
dir_list = os.listdir(dir)
for sub_dir in dir_list:
    sub_dir_name = dir + sub_dir + '/'
    sub_dir_list = os.listdir(sub_dir_name)
    for item in sub_dir_list:
        img = sub_dir_name + item
        try:
            image = Image.open(img)
            image = image.convert("YCbCr")
        except:
            print(img)
            continue
        else:
            r_image = yolo.detect_image(image)
            new_name = 'pic/' + sub_dir + item
            r_image.save(new_name)

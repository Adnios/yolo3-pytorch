#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
from yolo import YOLO
from PIL import Image
import time

yolo = YOLO()

while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        begin_time = time.time()
        r_image = yolo.detect_image(image)
        end_time = time.time()
        print(end_time - begin_time)
        r_image.show()

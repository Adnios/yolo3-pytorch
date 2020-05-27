from PIL import Image
import os

class Convert():
    def __init__(self):
        self.path = ''  # 存放图片的文件夹路径

    def convert(self):
        filelist = os.listdir(self.path)
        for item in filelist:
            if item.endswith('.jpg'):  # 图片格式为jpg
                file = self.path + '/' + item
                img = Image.open(file)
                print(img.mode)
                img = img.convert("YCbCr")
                print(img.mode)
                img.save(file)
                print(file)


if __name__ == '__main__':

    demo = Convert()
    file = '/mnt/d/temp/yolo3-pytorch-dvs/VOCdevkit/VOC2007/JPEGImages'
    demo.path =  file
    demo.convert()

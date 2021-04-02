import os

DATA_PATH = '/home/xiaoming/Desktop/Python_Project/YOLO_classroom/PyTorch-YOLOv3-master/data/coco/images/train2017/'

with open('trainvalno5k.txt','a') as file_handle:
    for _, _, file_name_list in os.walk(DATA_PATH):
        for filename in file_name_list:
            file_handle.write(DATA_PATH+str(filename))
            file_handle.write('\n')

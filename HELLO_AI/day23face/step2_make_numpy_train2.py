import numpy as np
import cv2
import random
from numpy import dtype
import os


labels = ["곽금규",
          "곽동석",
          "김민수",
          "심재린",
          "조정현"
          ]

dirs = [
        "00",
        "01",
        "02",
        "03",
        "04"
      ]

train_label = []
train_image = np.empty((0, 0, 0),np.uint8)

cnt = 0

for i in range(5):
    files = os.listdir("train_image/"+dirs[i])
    for f in files:
        train_image = np.append(train_image,cv2.imread('train_image/'+dirs[i]+'/{}'.format(f)))
        train_label.append(i)
        cnt+=1
    
    
# files = os.listdir("train_image/"+dirs[1])
# for f in files:
#     train_image = np.append(train_image,cv2.imread('train_image/'+dirs[1]+'/{}'.format(f)))
#     train_label.append(1)  
#     cnt+=1  
#
# files = os.listdir("train_image/02")
# for f in files:
#     train_image = np.append(train_image,cv2.imread('train_image/02/{}'.format(f)))
#     train_label.append(2)  
#     cnt+=1      

train_image = train_image.reshape((cnt,32,32,3))
train_label_n = np.array(train_label)

np.save("train_image1",train_image)
np.save("train_label1",train_label_n)






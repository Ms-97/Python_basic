import numpy as np
import cv2
import random
from numpy import dtype
import os

labels = ["곽금규m",
          "곽동석m",
          "기민혁m",
          "김미정m",
          "김민수m",
          
          "김성겸m",
          "김유미m",
          "박건영m",
          "박성우m",
          "박수빈m",
          
          "박수현m",
          "박지영m",
          "심재린m",
          "양형주m",
          "윤재열m",
          
          "이상권m",
          "이혜림m",
          "장재훈m",
          "조정현m",
          "채희진m",
          
          "최재혁m",
          "한재웅m",
          "한태훈m"
          ]

dirs = [
        "00",
        "01",
        "02",
        "03",
        "04",
        
        "05",
        "06",
        "07",
        "08",
        "09",
        
        "10",
        "11",
        "12",
        "13",
        "14",
        
        "15",
        "16",
        "17",
        "18",
        "19",
        
        "20",
        "21",
        "22"
      ]

train_label = []
train_image = np.empty((0, 0, 0),np.uint8)

cnt = 0

for i in range(23):
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

np.save("train_image",train_image)
np.save("train_label",train_label_n)






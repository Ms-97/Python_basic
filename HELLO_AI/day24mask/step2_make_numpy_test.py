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

test_label = []
test_image = np.empty((0, 0, 0),np.uint8)

cnt = 0

for i in range(23):
    files = os.listdir("test_image/"+dirs[i])
    for f in files:
        test_image = np.append(test_image,cv2.imread('test_image/'+dirs[i]+'/{}'.format(f)))
        test_label.append(i)
        cnt+=1
    
    


test_image = test_image.reshape((cnt,32,32,3))
test_label_n = np.array(test_label)

print(test_image.shape)
print(test_label_n)

np.save("test_image",test_image)
np.save("test_label",test_label_n)






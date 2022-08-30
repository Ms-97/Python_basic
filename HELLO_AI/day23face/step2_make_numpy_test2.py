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



test_label = []
test_image = np.empty((0, 0, 0),np.uint8)

cnt = 0

for i in range(5):
    files = os.listdir("test_image/"+dirs[i])
    for f in files:
        test_image = np.append(test_image,cv2.imread('test_image/'+dirs[i]+'/{}'.format(f)))
        test_label.append(i)
        cnt+=1
    
    


test_image = test_image.reshape((cnt,32,32,3))
test_label_n = np.array(test_label)

print(test_image.shape)
print(test_label_n)

np.save("test_image1",test_image)
np.save("test_label1",test_label_n)






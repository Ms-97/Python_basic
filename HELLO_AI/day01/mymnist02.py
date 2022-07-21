# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import cv2 
 
# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


for idx,img in enumerate(train_images):
    cv2.imwrite('train/'+str(idx)+'.jpg', train_images[idx])

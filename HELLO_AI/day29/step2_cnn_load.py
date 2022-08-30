
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
import cv2


labels_team = ["곽금규",
          "곽동석",
          "김민수",
          "심재린",
          "조정현"
          ]

labels = ["곽금규",
          "곽동석",
          "기민혁",
          "김미정",
          "김민수",
          
          "김성겸",
          "김유미",
          "박건영",
          "박성우",
          "박수빈",
          
          "박수현",
          "박지영",
          "심재린",
          "양형주",
          "윤재열",
          
          "이상권",
          "이혜림",
          "장재훈",
          "조정현",
          "채희진",
          
          "최재혁",
          "한재웅",
          "한태훈"
          ]





img1 = cv2.imread('mem4.jpg')
resize_img = cv2.resize(img1, (32,32))


print(resize_img.shape)

resize_img = np.reshape(resize_img,(1,32,32,3)) 

test_images = resize_img/255.0


model = tf.keras.models.load_model('face.h5')

predictions = model.predict(test_images)

for i in range(1):
    idx_label = np.argmax(predictions[i])
    print(i,labels[idx_label])



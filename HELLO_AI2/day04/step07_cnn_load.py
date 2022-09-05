

from tensorboard.compat import tf
import numpy as np
import cv2


labels = [
    "곽금규",
    "곽동석",
    "김민수",
    "심재린",
    "조정현"
  ]


img1 = cv2.imread('output.png')

print("img1",img1.shape)

resize_img = img1.reshape((1,480,640,3)) 
train_images = resize_img/255.0


model = tf.keras.models.load_model('myvoice.h5')

predictions = model.predict(train_images)
l_idx = np.argmax(predictions[0])

print(l_idx,labels[l_idx])



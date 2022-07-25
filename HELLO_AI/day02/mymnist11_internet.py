
from tensorboard.compat import tf
import numpy as np
import cv2

img1 = cv2.imread('9.jpg')
resize_img = cv2.resize(img1, (28, 28))
train_images = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
train_images = 255 - train_images
train_images = 1 - train_images
print(train_images.shape)



model = tf.keras.models.load_model('mnist.h5')

predicted_result = model.predict(train_images)

ai_answer = np.argmax(predicted_result[0])
print("ai_answer",ai_answer)
import tensorflow as tf
import numpy as np
from keras import models
from keras import layers
from keras.utils import to_categorical
import cv2


fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

for idx, l in enumerate(train_labels):
    label = train_labels[idx]
    print(f'train/{label}/{idx}.jpg')
    cv2.imwrite(f'train/{label}/{idx}.jpg',train_labels[idx])
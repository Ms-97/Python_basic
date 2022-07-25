import tensorflow as tf
import numpy as np
import cv2


fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

for idx, i in enumerate(train_labels):
    label = train_labels[idx]
    print(f'train/{label}/{idx}.jpg')
    cv2.imwrite(f'train/{label}/{idx}.jpg',train_images[idx])
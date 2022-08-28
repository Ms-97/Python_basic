import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models, layers


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

train_images = np.load("train_image.npy")
train_labels = np.load("train_label.npy")
test_images = np.load("test_image.npy")
test_labels = np.load("test_label.npy")

print("Train samples:", train_images.shape, train_labels.shape)
print("Test samples:", test_images.shape, test_labels.shape)
 

train_images = train_images/255.0
test_images = test_images/255.0

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(23, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)
model.save("face_m.h5")

test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

predictions = model.predict(test_images)

for i in range(927):
    print(i,np.argmax(predictions[i]))







from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np

train_images = np.load("omok_train.npy")
train_labels = np.load("omok_answer.npy")


train_labels_c = to_categorical(train_labels)
print("train_labels_c",train_labels_c)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(400,)))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(400, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])


model.fit(train_images[0:9], train_labels_c[0:9], epochs=20)

predict_result = model.predict(train_images[0:9])
print("predict_result",predict_result)
for r in predict_result:
    ai_answer = np.argmax(r)
    ii = int(ai_answer / 20)
    jj = ai_answer % 20
    print(ai_answer,ii,jj,end=",")
    print()





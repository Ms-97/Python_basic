# 필요한 라이브러리 불러오기
import numpy as np
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
  
# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

g_train_labels = train_labels
 
# 이미지 데이터 준비하기 (모델에 맞는 크기로 바꾸고 0과 1사이로 스케일링)
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255
 
# 레이블을 범주형으로 인코딩
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
 
# 모델 정의하기 (여기에서는 Sequential 클래스 사용)
model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))
 
# 모델 컴파일 하기
model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
                                        
# fit() 메서드로 모델 훈련 시키기
model.fit(train_images, train_labels, epochs=10, batch_size=128)
test_loss, test_acc = model.evaluate(test_images, test_labels) 
print('test_acc', test_acc)
 
predicted_result = model.predict(train_images)

cnt_o = 0
cnt_x = 0

for i in range(60000):
    go_label = g_train_labels[i]
    ai_label = np.argmax(predicted_result[i])
    if go_label == ai_label:
        cnt_o+=1
    else:
        cnt_x+=1  
        
#for idx,i in enumerate(g_train_labels):
#    if g_train_labels[idx] == np.argmax(predicted_result[idx]):
#        cnt_o+=1
#    else:
#        cnt_x+=1   


print("cnt_o ",cnt_o/60000)
print("cnt_x ",cnt_x/60000)
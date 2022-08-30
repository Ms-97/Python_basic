
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical
from tensorboard.compat import tf
import numpy as np


class Load:
    
    def __init__(self):
        pass
    
    def getNum(self,train_images):
        
        train_images = train_images/255.0
        
        model = tf.keras.models.load_model('face_3.h5')
        
        predictions = model.predict(train_images)
           
        return np.argmax(predictions[0])
            
if __name__ == '__main__':
    pass
    

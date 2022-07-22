
from tensorboard.compat import tf
import numpy as np
from tensorflow import keras





image = tf.keras.preprocessing.image.load_img("0_0_1.png")
input_arr = keras.preprocessing.image.img_to_array(image)
input_arr = np.array([input_arr])

model = tf.keras.models.load_model('mnist.h5')

predicted_result = model.predict(input_arr)

ai_answer = np.argmax(predicted_result[0])
print("ai_answer",ai_answer)
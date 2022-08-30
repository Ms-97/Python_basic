from tensorboard.compat import tf
import numpy as np
from day27_menu2db.daomenu import DaoMenu

dao = DaoMenu()

labels = dao.getGroupMenu()

train_images_a = [
    [4,9]
]

train_images_n = np.array(train_images_a)
train_images_n = train_images_n / (len(labels)-1)


model = tf.keras.models.load_model('2.h5')

predictions = model.predict(train_images_n)

idx =np.argmax(predictions[0])
print(labels[idx])

    
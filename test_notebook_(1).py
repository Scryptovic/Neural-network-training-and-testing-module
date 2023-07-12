# -*- coding: utf-8 -*-
"""Test_Notebook_(1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ONQkRYfXAcuU0pHAMdBBhB9Xacz6AV-N

# Сейчас мы запустим этот тестовый ноутбук!

Text
"""

import numpy as np
import tensorflow as tf
import pandas as pd

from tensorflow.keras.datasets import mnist

import tensorflow as tf

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(117, activation='relu'),
        # Вставляем свой слой с весами
        tf.keras.layers.Dense(117, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model

# Создание модели
model = create_model()

# Загрузка эксель файла
df = pd.read_excel('/content/weights.xlsx')

# Округление значений до 4 знаков после запятой
df = df.round(4)

# Сохранение изменений в новый эксель файл
df.to_excel('newweights.xlsx', index=False)

weights = model.get_weights()

weights

# Загрузка весов из файла Excel
weights_file = "newweights.xlsx"
weights_df = pd.read_excel(weights_file, header=None)

# Преобразование весов в массив numpy
weights = weights_df.to_numpy(dtype=np.float32)



# Замена весов между первым и вторым скрытыми слоями
model.layers[2].set_weights([weights, np.zeros(117, dtype=np.float32)])
model.set_weights(weights)
# Компиляция модели
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

weights = model.get_weights()
weights

# Загрузка данных MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Нормализация данных
train_images = train_images / 255.0
test_images = test_images / 255.0




# Обучение модели
model.fit(train_images, train_labels, epochs=10, batch_size=32, validation_data=(test_images, test_labels))

# Оценка точности модели на тестовых данных
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print('Test loss:', test_loss)
print('Test accuracy:', test_accuracy)

weights = model.get_weights()
weights
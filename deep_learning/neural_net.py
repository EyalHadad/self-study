from keras.datasets import mnist
from keras.utils import to_categorical
from keras import models
from keras import layers
import numpy as np
import matplotlib.pyplot as plt




def run_func():
    (train_img, train_labels), (test_img, test_labels) = mnist.load_data()
    network = models.Sequential()
    network.add(layers.Dense(512,activation='relu', input_shape=(28*28, )))
    network.add(layers.Dense(10,activation='softmax'))
    network.compile(optimizer='rmsprop', loss='categorical_crossentropy',
                    metrics=['accuracy'])

    train_img = train_img.reshape((60000,28*28))
    train_img = train_img.astype('float32') / 255
    test_img = test_img.reshape((10000,28*28))
    test_img = test_img.astype('float32') / 255

    train_labels = to_categorical(train_labels)
    test_labels = to_categorical(test_labels)
    network.fit(train_img,train_labels,epochs=5,batch_size=128)
    test_loss, test_acc = network.evaluate(test_img,test_labels)
    print("test acc: " + str(test_acc))

    i=5


def tmp_tries():
    (train_img, train_labels), (test_img, test_labels) = mnist.load_data()
    digit = train_img[4]
    # plt.imshow(digit,cmap=plt.cm.binary)
    # plt.show()
    i=5


if __name__ == '__main__':
    # tmp_tries()
    run_func()


from keras.applications import VGG16
import os
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras import models
from keras import layers
from keras import optimizers

def extract_features(path,sample_count, datagen, batch_size,conv_base):
    features = np.zeros(shape=(sample_count, 4, 4, 512))
    labels = np.zeros(shape=sample_count)
    generator = datagen.flow_from_directory(path,target_size=(150,150), batch_size= batch_size, class_mode = 'binary')
    i=0
    for input_batch, labels_batch in generator:
        features_batch = conv_base.predict(input_batch)
        features[i*batch_size : (i+1) * batch_size] = features_batch
        labels[i * batch_size: (i + 1) * batch_size] = labels_batch
        i+=1
        if i*batch_size >= sample_count:
            break
    return features,labels


def create_and_train_simple_model(train_features,train_labels,validation_features,validation_labels):
    model = models.Sequential()
    model.add(layers.Dense(256, activation='relu', input_dim=4*4*512))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=optimizers.RMSprop(lr=2e-5), metrics=['acc'])
    history = model.fit(train_features,train_labels,epochs=30,batch_size=20,validation_data=(validation_features,validation_labels))
    return model,history

def show_results(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(acc) + 1)

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and Validation accuracy')
    plt.legend() # for the two lines, can get parameters such as loc='upper left' for locating the lines "menu"

    plt.figure()

    plt.plot(epochs, loss, 'b', label='Training loss')
    plt.plot(epochs, val_loss, 'bo', label='Validation loss')
    plt.title('Training and Validation loss')
    plt.legend()

    plt.show()



def pretrained_model_no_augmentation(b_dir):
    train_dir = os.path.join(b_dir, 'train')
    valid_dir = os.path.join(b_dir, 'validation')
    test_dir = os.path.join(b_dir, 'test')
    datagen = ImageDataGenerator(rescale=1. / 255)
    conv_base = VGG16(weights='imagenet', include_top=False, input_shape=(150, 150, 3))
    # weights what weights to use (from what network)
    # include_top means using or not the dense layers
    t_features, t_labels = extract_features(train_dir, sample_count=2000, datagen=datagen, batch_size=20,conv_base=conv_base)
    v_features, v_labels = extract_features(valid_dir, sample_count=1000, datagen=datagen, batch_size=20,conv_base=conv_base)
    test_features, test_labels = extract_features(test_dir, sample_count=1000, datagen=datagen, batch_size=20,conv_base=conv_base)
    t_features = np.reshape(t_features, (2000,4*4*512))
    v_features = np.reshape(v_features, (1000,4*4*512))
    test_features = np.reshape(test_features, (1000,4*4*512))
    #Those features (images representation) can be saved to the disk and be used many times later

    model,history = create_and_train_simple_model(t_features,t_labels,v_features,v_labels)
    show_results(history)
    i=4









if __name__ == '__main__':
    base_dir =r'C:\Users\Eyal-TLV\Desktop\Studies\cats_dogs'
    pretrained_model_no_augmentation(base_dir)




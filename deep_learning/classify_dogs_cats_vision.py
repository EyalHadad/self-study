import os
import shutil
from keras import layers, models, optimizers
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import pickle
import h5py
from keras.models import load_model



def arrange_data(original_dataset_dir, base_dir):
    os.mkdir(base_dir)

    train_dir = os.path.join(base_dir, 'train')
    os.mkdir(train_dir)
    valid_dir = os.path.join(base_dir, 'validation')
    os.mkdir(valid_dir)
    test_dir = os.path.join(base_dir, 'test')
    os.mkdir(test_dir)

    train_dogs_dir = os.path.join(train_dir, 'dogs')
    os.mkdir(train_dogs_dir)
    train_cats_dir = os.path.join(train_dir, 'cats')
    os.mkdir(train_cats_dir)

    valid_dogs_dir = os.path.join(valid_dir, 'dogs')
    os.mkdir(valid_dogs_dir)
    valid_cats_dir = os.path.join(valid_dir, 'cats')
    os.mkdir(valid_cats_dir)

    test_dogs_dir = os.path.join(test_dir, 'dogs')
    os.mkdir(test_dogs_dir)
    test_cats_dir = os.path.join(test_dir, 'cats')
    os.mkdir(test_cats_dir)

    copy_pictures(original_dataset_dir, train_cats_dir, 'cat', 0, 1000)
    copy_pictures(original_dataset_dir, valid_cats_dir, 'cat', 1000, 1500)
    copy_pictures(original_dataset_dir, test_cats_dir, 'cat', 1500, 2000)
    copy_pictures(original_dataset_dir, train_dogs_dir, 'dog', 0, 1000)
    copy_pictures(original_dataset_dir, valid_dogs_dir, 'dog', 1000, 1500)
    copy_pictures(original_dataset_dir, test_dogs_dir, 'dog', 1500, 2000)
    return [train_dogs_dir, train_cats_dir, valid_dogs_dir, valid_cats_dir, test_dogs_dir, test_cats_dir]


def copy_pictures(original_dataset_dir, dest_dir, animal_name, s_index, e_index):
    fnames = [animal_name + '.{}.jpg'.format(i) for i in range(s_index, e_index)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(dest_dir, fname)
        shutil.copyfile(src, dst)


def create_model():
    model = models.Sequential()
    model.add(
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))  # input shape just for first layer
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))  # first argument is the number of filters -> increase
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))  # second argument is filter size
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPool2D((2, 2)))
    model.add(layers.Flatten())  # multiple all layer sizes
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=optimizers.RMSprop(lr=1e-4), metrics=['acc'])  # crossentropy
    #  because it's binary classification, metrics used to judge our model and not to make it better
    return model


def data_preprocessing(train_dir, validation_dir):
    train_datagen = ImageDataGenerator(rescale=1. / 255)  # ImageDataGenerator is keras image processing tool
    test_datagen = ImageDataGenerator(rescale=1. / 255)  # resacle all images by 1/255 (values in [0,1] range)
    # we create generator function that yeild every time picture in format that we want
    # it generates 20 images every time, and each one in size of 150*150 in RGB mode (20,150,150,3)
    # because of batch size 20 it generate labels with shape: (20,)
    t_generator = train_datagen.flow_from_directory(train_dir, target_size=(150, 150), batch_size=20,
                                                        class_mode='binary')  # resize all images to 150*150, and
    # because we use binary_crossentropy we need binary labels

    val_generator = test_datagen.flow_from_directory(validation_dir, target_size=(150, 150), batch_size=20,
                                                            class_mode='binary')
    return t_generator, val_generator


def train_and_save_model(train_gen, validation_gen):
    model = create_model()
    history = model.fit(train_gen, steps_per_epoch=100, epochs=30, validation_data=validation_gen, validation_steps=50)
    # steps_per_epochs is the number of batches needed to finish one epoch (batch size set to be 20 when we define
    # the generator) - it is important because it generate endless data
    # validation_data not necessarily a generator
    # validation_steps - how many batches the validation include (50 batches of 20 images)
    model.save('cats_and_dogs_small_1.h5')
    with open('/trainHistoryDict', 'wb') as file_pi:
        pickle.dump(history.history, file_pi)
    return history


def show_results(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(acc) + 1)

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and Validation accuracy')
    plt.legend() # for the two lines, can get parameters such as loc='upper left' fro locating the lines "menu"

    plt.figure()

    plt.plot(epochs, loss, 'b', label='Training loss')
    plt.plot(epochs, val_loss, 'bo', label='Validation loss')
    plt.title('Training and Validation loss')
    plt.legend()

    plt.show()

if __name__ == '__main__':
    # m = create_model()
    # paths = arrange_data(r'C:\Users\user\Desktop\source_cat_dog', r'C:\Users\user\Desktop\cats_dogs')
    train_dir = os.path.join(r'C:\Users\user\Desktop\cats_dogs', 'train')
    valid_dir = os.path.join(r'C:\Users\user\Desktop\cats_dogs', 'validation')
    train_generator, validation_generator = data_preprocessing(train_dir, valid_dir)
    his_dict = train_and_save_model(train_generator, validation_generator)
    show_results(his_dict)
    i = 5

import os
import shutil
from keras import layers, models, optimizers
from keras.preprocessing import image
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
    model.add(layers.Dropout(0.5))
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


def train_and_save_model(train_path, validation_path):
    model = create_model()
    #define generators
    train_datagen = ImageDataGenerator(rescale=1./255,rotation_range=40,width_shift_range=0.2,height_shift_range=0.2,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,fill_mode='nearest')
    test_datagen = ImageDataGenerator(rescale=1./255) # validation data shouldn't be augmented
    # use the generators
    t_generator = train_datagen.flow_from_directory(train_path, target_size=(150, 150), batch_size=32,class_mode='binary')
    v_generator = test_datagen.flow_from_directory(validation_path, target_size=(150, 150), batch_size=32,class_mode='binary')


    history = model.fit_generator(t_generator, steps_per_epoch=100, epochs=100, validation_data=v_generator, validation_steps=50)
    # steps_per_epochs is the number of batches needed to finish one epoch (batch size set to be 20 when we define
    # the generator) - it is important because it generate endless data
    # validation_data not necessarily a generator
    # validation_steps - how many batches the validation include (50 batches of 20 images)
    model.save('cats_and_dogs_small_2.h5')
    with open('trainHistoryDict', 'wb') as file_pi:
        pickle.dump(history, file_pi)
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
    plt.legend() # for the two lines, can get parameters such as loc='upper left' for locating the lines "menu"

    plt.figure()

    plt.plot(epochs, loss, 'b', label='Training loss')
    plt.plot(epochs, val_loss, 'bo', label='Validation loss')
    plt.title('Training and Validation loss')
    plt.legend()

    plt.show()


def get_model_history():
    loaded_model = load_model('cats_and_dogs_small_1.h5')
    with open('trainHistoryDict', 'rb') as file_pi:
        history = pickle.load(file_pi)

    return history, loaded_model


def augment_picture(train_path):
    datagen = ImageDataGenerator(rotation_range=40,width_shift_range=0.2,height_shift_range=0.2,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,fill_mode='nearest')
    #rotation_range range within which to randomly rotate pictures
    #hight/width_shift how mush to make the picture higher or wider
    #shear/zoom_range how much to cut/zoom into the picture
    #horizontal_flip randomly flip half of the picture horizontally
    #fill_mode strategy used for filling newly created pixels, which can appear after rotation
    train_cats_dir = os.path.join(train_path, 'cats')
    fnames = [os.path.join(train_cats_dir,fname) for fname in os.listdir(train_cats_dir)]
    img = image.load_img(fnames[3],target_size=(150,150)) #reads the image and resizes it
    x = image.img_to_array(img) #convert the image into np array with shape of (150,150,3) due to the resize parameter and the RGB mode
    x = x.reshape((1,) + x.shape) #reshape it into (1,150,150,3)
    i=0
    for batch in datagen.flow(x,batch_size=1):
        plt.figure(i)
        imgplot = plt.imshow(image.array_to_img(batch[0]))
        i += 1
        if i%4 ==0:
            break
    plt.show()


if __name__ == '__main__':
    # paths = arrange_data(r'C:\Users\Eyal-TLV\Desktop\Studies\cats_dogs_orig\train', r'C:\Users\Eyal-TLV\Desktop\Studies\cats_dogs')
    train_dir = os.path.join(r'C:\Users\Eyal-TLV\Desktop\Studies\cats_dogs', 'train')
    valid_dir = os.path.join(r'C:\Users\Eyal-TLV\Desktop\Studies\cats_dogs', 'validation')
    # train_generator, validation_generator = data_preprocessing(train_dir, valid_dir) # redundant stay just for explanations
    # augment_picture(train_dir)# redundant stay just for explanations
    his_dict = train_and_save_model(train_dir, valid_dir)
    # his_dict,l_model = get_model_history()
    show_results(his_dict)
    i = 5

import matplotlib.pyplot as plt
from keras.datasets import boston_housing
import numpy as np
from keras import models
from keras import layers


def process_data():
    (train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()
    print("train data shape:" + str(train_data.shape))
    print("test data shape:" + str(test_data.shape))

    mean = train_data.mean(axis = 0)
    train_data -= mean
    std = train_data.std(axis=0)
    train_data /= std
    test_data -= mean
    test_data /= std

    k=4
    num_val_samples = len(train_data) // 4
    num_epochs = 100
    all_mae_history = []
    for i in range(k):
        print('processing fold #', i)
        val_data = train_data[i*num_val_samples: (i+1) * num_val_samples]
        val_targets = train_targets[i * num_val_samples: (i + 1) * num_val_samples]
        partial_train_data = np.concatenate(
            [train_data[: i * num_val_samples],train_data[(i+1) * num_val_samples : ]], axis = 0
        )

        partial_train_targets = np.concatenate(
            [train_targets[: i * num_val_samples], train_targets[(i + 1) * num_val_samples:]], axis=0
        )
        model = build_model(train_data)
        history = model.fit(partial_train_data, partial_train_targets, validation_data =(val_data,val_targets) ,epochs=num_epochs,batch_size=1, verbose=0)
        mae_history = history.history['val_mean_absolute_error']
        all_mae_history.append(mae_history)

    avg_mae_history = [np.mean([x[i] for x in all_mae_history]) for i in range(num_epochs)]
    show_mae_plot(avg_mae_history)


def build_model(train_data):
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model


def show_acc_plot(history_dict):
    plt.clf()
    acc_values = history_dict['acc']
    val_acc_values = history_dict['val_acc']
    epochs = range(1, len(history_dict['acc']) + 1)
    plt.plot(epochs, acc_values, 'bo', label='Training acc')
    plt.plot(epochs, val_acc_values, 'b', label='Validation acc')
    plt.title('Training and validation acc')
    plt.xlabel('Epochs')
    plt.ylabel('Acc')
    plt.legend()
    plt.show()


def show_mae_plot(average_mae_history):
    plt.plot(range(1, len(average_mae_history) + 1),average_mae_history)
    plt.title('Mae')
    plt.xlabel('Epochs')
    plt.ylabel('Validation MAE')
    plt.show()

if __name__ == '__main__':
    process_data()


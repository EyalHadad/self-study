import keras
from keras import layers
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.utils import plot_model


def run_tensorBoard():
    max_features = 2000
    max_len = 500
    LOG_PATH = r'C:\Users\Eyal-TLV\Desktop\Studies\self-study\deep_learning\logs'
    (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
    x_train = sequence.pad_sequences(x_train, maxlen=max_len)
    x_test = sequence.pad_sequences(x_test, maxlen=max_len)
    model = keras.models.Sequential()
    model.add(layers.Embedding(max_features, 128, input_length=max_len, name='embed'))
    model.add(layers.Conv1D(32, 7, activation='relu'))
    model.add(layers.MaxPooling1D(5))
    model.add(layers.Conv1D(32, 7, activation='relu'))
    model.add(layers.GlobalMaxPool1D())
    model.add(layers.Dense(1))
    model.summary()
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
    callbacks = [keras.callbacks.TensorBoard(log_dir=LOG_PATH,histogram_freq=1,embeddings_freq=1)]
    history = model.fit(x_train,y_train,epochs=20,batch_size=128,validation_split=0.2,callbacks=callbacks)
    plot_model(model,to_file='model.png')


if __name__=='__main__':
    run_tensorBoard()

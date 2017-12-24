import dataset_preproces as dp
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from utils.cache import cache
from config import basedir


def train_trans_d_model(name):
    type = "trans_d"

    log_dir = basedir + '/' + type + '/' + name

    data = dp.pp_trans_d_for_model(name)
    train_X = data['train_X']
    train_Y = data['train_Y']
    valid_X = data['valid_X']
    valid_Y = data['valid_Y']
    test_X = data['test_X']
    test_Y = data['test_Y']
    num_classes = 22

    model = Sequential()
    model.add(Dense(32, input_dim=15, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(num_classes, activation='relu'))

    # For a multi-class classification problem
    optimizer = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-8)

    model.compile(optimizer=optimizer,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Train the model, iterating on the data in batches of 32 samples

    one_hot_labels = keras.utils.to_categorical(train_Y, num_classes=num_classes)

    one_hot_valid_Y = keras.utils.to_categorical(valid_Y, num_classes=num_classes)

    print(one_hot_labels.shape)
    print(one_hot_labels[1])

    # TensorBoard回调，开启之后会比较卡
    # tb_cb = keras.callbacks.TensorBoard(log_dir=log_dir, write_images=1, histogram_freq=1)
    callbacks = []
    # callbacks.append(tb_cb)

    model.fit(train_X,
              one_hot_labels,
              epochs=20,
              batch_size=64,
              callbacks=callbacks,
              validation_data=(valid_X, one_hot_valid_Y))
    return model


name = "过去一年每日交易数据集"
train_trans_d_model(name)

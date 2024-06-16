import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, TensorBoard
from keras.optimizers import Adam
from keras.layers import (Conv2D, Flatten, MaxPooling2D, Input, 
                          BatchNormalization, Dropout, Dense, InputLayer, GlobalAveragePooling2D)
from keras.models import Model

def create_combined_model(input_shape=(48, 48, 1), num_classes=8):
    vgg16_base = tf.keras.applications.VGG16(weights='imagenet', include_top=False, input_shape=(48, 48, 3))

    input_layer = tf.keras.layers.Input(shape=input_shape)
    x = tf.keras.layers.Conv2D(3, (1, 1), padding='same')(input_layer)  # Repeat grayscale channel to 3 channels
    x = vgg16_base(x)

    # Custom layers added after VGG16
    x = Conv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.4)(x)

    x = Conv2D(filters=384, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.4)(x)  # Removed pooling to prevent dimension reduction

    x = Conv2D(filters=192, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.4)(x)

    x = Conv2D(filters=384, kernel_size=(3, 3), activation='relu', padding='same')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.4)(x)

    # Instead of MaxPooling, we use GlobalAveragePooling2D to handle the dimensions properly
    x = GlobalAveragePooling2D()(x)

    x = Dense(256, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)

    output_layer = Dense(num_classes, activation='softmax')(x)

    return Model(inputs=input_layer, outputs=output_layer, name='combined_model')
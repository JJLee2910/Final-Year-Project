import tensorflow as tf
from keras.applications import VGG16
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, InputLayer, Input

def create_model(num_classes):
    # Load pre-trained VGG16 model
    vgg16_base = VGG16(weights='imagenet', include_top=False, input_shape=(48, 48, 3))
    
    # Create a new model
    model = Sequential()
    
    # Add an input layer to match the grayscale input, and repeat the channels to match the VGG16 expected input shape
    model.add(InputLayer(input_shape=(48, 48, 1)))
    model.add(Conv2D(3, (1, 1), padding='same'))  # Repeat the single channel to three channels
    
    # Add the pre-trained VGG16 base model
    model.add(vgg16_base)
    
    # Flatten the output of VGG16 base model
    model.add(Flatten())
    
    # Add new fully connected layers
    model.add(Dense(256, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))  # num_classes in FER2013 dataset
    
    return model
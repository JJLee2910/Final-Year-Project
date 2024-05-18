import os
import pickle
from keras.callbacks import EarlyStopping, TensorBoard
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
import tensorflow as tf
from keras.applications import ResNet50
from keras.layers import Dense, Dropout, GlobalAveragePooling2D, BatchNormalization, Input
from keras.models import Model

def create_resnet_model(input_shape=(48, 48, 1), num_classes=7):
    # Load the ResNet50 model, excluding the top layer
    base_model = ResNet50(weights=None, include_top=False, input_shape=input_shape)
    
    # Adding custom layers on top of the ResNet50 base model
    x = base_model.output
    x = GlobalAveragePooling2D()(x)  # Global average pooling layer
    x = Dense(256, activation='relu')(x)  # Dense layer with ReLU activation
    x = BatchNormalization()(x)  # Batch normalization layer
    x = Dropout(0.3)(x)  # Dropout layer for regularization
    predictions = Dense(num_classes, activation='softmax')(x)  # Final output layer with softmax activation

    # Create the final model
    model = Model(inputs=base_model.input, outputs=predictions, name='resnet_model')

    return model

def train():
    log_dir = './Log'
    train_dataset_path = r"Data/train"
    val_dataset_path = r'Data/val'
    test_dataset_path = r"Data/test"
    batch_size = 128
    lr = 1e-3
    epochs = 50
    num_classes = 7

    train_datagen = ImageDataGenerator(
        rescale=1 / 255.0,
        rotation_range=10,
        zoom_range=0.1,
        horizontal_flip=True
    )

    train_generator = train_datagen.flow_from_directory(
        directory=train_dataset_path,
        target_size=(48, 48),
        color_mode="grayscale",
        batch_size=batch_size,
        class_mode="categorical",
        shuffle=True,
        seed=42
    )

    test_datagen = ImageDataGenerator(rescale=1 / 255.0)

    valid_generator = test_datagen.flow_from_directory(
        directory=val_dataset_path,
        target_size=(48, 48),
        color_mode="grayscale",
        class_mode="categorical",
        batch_size=batch_size,
        shuffle=True,
        seed=42
    )

    test_generator = test_datagen.flow_from_directory(
        directory=test_dataset_path,
        target_size=(48, 48),
        color_mode="grayscale",
        class_mode="categorical",
        batch_size=batch_size,
        shuffle=True,
        seed=42
    )

    # Create the ResNet model
    model = create_resnet_model(input_shape=(48, 48, 1), num_classes=num_classes)

    model.summary()
    
    early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=10, verbose=1)
    tensorboard = TensorBoard(log_dir=log_dir)
    
    optimizer = Adam(learning_rate=lr)
    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer=optimizer)
    
    model_info = model.fit(train_generator, validation_data=valid_generator,
                           epochs=epochs, callbacks=[tensorboard, early_stopping])
    
    model.evaluate(test_generator, verbose=1)
    model.save('./resnet_model.h5')

    # Saving history
    history = {
        'loss': model_info.history['loss'],
        'acc': model_info.history['accuracy'],
        'val_loss': model_info.history['val_loss'],
        'val_acc': model_info.history['val_accuracy']
    }
    
    with open('resnet_model.pkl', 'wb') as f:
        pickle.dump(history, f)

if __name__ == '__main__':
    train()

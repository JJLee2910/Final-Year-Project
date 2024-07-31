
# import required packages
import cv2
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import TensorBoard
from keras.utils import plot_model

# Initialize image data generator with rescaling
train_data_gen = ImageDataGenerator(rescale=1./255)
validation_data_gen = ImageDataGenerator(rescale=1./255)

tensorboard_callback = TensorBoard(log_dir='./based_model', histogram_freq=1)

# Preprocess all train images
train_generator = train_data_gen.flow_from_directory(
        'Data/train',
        target_size=(48, 48),
        batch_size=128,
        color_mode="grayscale",
        class_mode='categorical')

# Preprocess all test images
validation_generator = validation_data_gen.flow_from_directory(
        'Data/val',
        target_size=(48, 48),
        batch_size=128,
        color_mode="grayscale",
        class_mode='categorical')

# create model structure
emotion_model = Sequential()

emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(8, activation='softmax'))

cv2.ocl.setUseOpenCL(False)
optimizer = Adam(learning_rate=0.0001)
emotion_model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

emotion_model.summary()

plot_model(emotion_model, show_shapes = True, show_layer_names = True)

# Train the neural network/model
emotion_model_info = emotion_model.fit(
        train_generator,
        steps_per_epoch=32645 // 128,
        epochs=50,
        validation_data=validation_generator,
        validation_steps=8166 // 128,
        callbacks=[tensorboard_callback])

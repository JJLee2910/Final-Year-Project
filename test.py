# import required packages
import cv2
from keras.applications.vgg16 import VGG16
from keras.layers import Dense, Dropout, Flatten
from keras.models import Model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
import pickle

# Initialize image data generator with rescaling
train_data_gen = ImageDataGenerator(rescale=1./255)
validation_data_gen = ImageDataGenerator(rescale=1./255)

# Preprocess all train images
train_generator = train_data_gen.flow_from_directory(
    'data/train',
    target_size=(48, 48),
    batch_size=64,
    color_mode="rgb",  # Change to 'rgb' for RGB images
    class_mode='categorical')

# Preprocess all test images
validation_generator = validation_data_gen.flow_from_directory(
    'data/test',
    target_size=(48, 48),
    batch_size=64,
    color_mode="rgb",  # Change to 'rgb' for RGB images
    class_mode='categorical')

# Load the pre-trained VGG16 model without the top classification layers
vgg_model = VGG16(weights='imagenet', include_top=False, input_shape=(48, 48, 3))

# Freeze the pre-trained layers
for layer in vgg_model.layers:
    layer.trainable = False

# Add custom classification layers
x = vgg_model.output
x = Flatten()(x)
x = Dense(1024, activation='relu')(x)
x = Dropout(0.5)(x)
x = Dense(7, activation='softmax')(x)

# Create the final model
emotion_model = Model(inputs=vgg_model.input, outputs=x)

# Compile the model
optimizer = Adam(learning_rate=0.0001)
emotion_model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# Train the model
emotion_model_info = emotion_model.fit_generator(
    train_generator,
    steps_per_epoch=28709 // 64,
    epochs=50,
    validation_data=validation_generator,
    validation_steps=7178 // 64)

# Save the model structure and weights
model_json = emotion_model.to_json()
with open("emotion_model.json", "w") as json_file:
    json_file.write(model_json)

emotion_model.save_weights('emotion_model.h5')

# Save the history object
with open('emotion_model_history.pkl', 'wb') as f:
    pickle.dump(emotion_model_info.history, f)
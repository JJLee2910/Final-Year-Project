from Model.vgg_model import create_model
from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np

emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised", 7:"Contempt"}

emotion_model = create_model(num_classes=8)
emotion_model.load_weights("Model/VGG16/vgg16_model.h5")

test_datagen = ImageDataGenerator(rescale=1 / 255.0)

valid_generator = test_datagen.flow_from_directory(
    directory="Data\\val",
    target_size=(48, 48),
    color_mode="grayscale",
    class_mode="categorical",
    batch_size=128,
    shuffle=False
)

steps_per_epoch = np.ceil(valid_generator.samples / valid_generator.batch_size).astype(int)

predictions = emotion_model.predict(valid_generator, steps=steps_per_epoch)

predictions = predictions[:valid_generator.samples]

# for result in predictions:
#     max_index = int(np.argmax(result))
#     print(emotion_dict[max_index])

print("-----------------------------------------------------------------")
# Confusion matrix
c_matrix = confusion_matrix(valid_generator.classes, predictions.argmax(axis=1))
print(c_matrix)
cm_display = ConfusionMatrixDisplay(confusion_matrix=c_matrix, display_labels=[emotion_dict[i] for i in range(8)])
cm_display.plot(cmap=plt.cm.Blues)
plt.show()

# Classification report
print("-----------------------------------------------------------------")
print(classification_report(valid_generator.classes, predictions.argmax(axis=1)))
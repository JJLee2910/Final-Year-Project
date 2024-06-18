import cv2
import numpy as np
from tensorflow import keras
from keras.models import load_model # type: ignore
from model import create_model
# from Validator.VGG16.vgg_model import create_model
# from Validator.VGG_CNN.vgg_cnn import create_combined_model


emotion_dict = {0: "Angry", 1: "Contempt", 2: "Disgust", 3: "Fear", 4: "Happy", 5: "Neutral", 6: "Sad", 7:"Surprise"}

num_classes = 8
emotion_model = create_model(num_classes=num_classes)

# extracting features from the image
def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0

# load weights into new model
emotion_model.load_weights("model3.h5")
print("Loaded model from disk")

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
# start the webcam feed
cap = cv2.VideoCapture(0)

while True:
    # Find haar cascade to draw bounding box around face
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    # take each face available on the camera and Preprocess it
    for (x, y, w, h) in faces:
        roi_gray_frame = gray[y:y + h, x:x + w]
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 4)
        image = cv2.resize(roi_gray_frame, (48, 48))

        img = extract_features(image)
        # predict the emotions
        emotion_prediction = emotion_model.predict(img)
        emotion_prob = np.max(emotion_prediction)
        emotion_text = f"{emotion_dict[emotion_prediction.argmax()]}: {emotion_prob:.2f}"
        cv2.putText(frame, emotion_text, (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Emotion Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Final-Year-Project
## Project Description
This project aims to develop a facial emotion recognition system that leverages optimized Convolutional Neural Networks (CNNs) to achieve better accuracy on the Facial Emotion Recognition (FER) dataset. The system explores various models, including VGG16 and a hybrid model combining CNN with Vision Transformers (ViT). It is developed using PyQt5 for the user interface, stores user details in MongoDB, and is designed following the MVC (Model-View-Controller) architecture.

## Features
- Facial emotion detection and recognition
- Real-time emotion tracking across 8 emotional classes
- User data management with MongoDB
- PyQt5-based graphical user interface
- Optimized CNN for enhanced accuracy
- Exploration of VGG16 and hybrid (CNN+ViT) models
- MVC architecture for modular and scalable design

## Usage
1. Start the application.
2. Register or log in as a user.
3. Use the system to detect and track facial emotions.
4. View the emotion count and trends on the GUI.

## Data
The system uses the [FER dataset](https://www.kaggle.com/datasets/prajwalsood/google-fer-image-format/data) for training and validation. The data is preprocessed and augmented to improve model accuracy. The dataset includes grayscale images with dimensions of 48x48 pixels.

## System Architecture
### MVC Architecture
1. Model: Represents the data and the business logic. This system includes the CNN models (VGG16, CNN+ViT) and the MongoDB database for storing user information.
2. View: The user interface developed using PyQt5, displays real-time emotion detection and other user data.
3. Controller: Manages the flow of data between the Model and View. The db.py file specifically handles data management, including database interactions and data retrieval.

## Future Work
1. Expand the system to recognize a broader range of emotions.
2. Improve the user interface for better usability.
3. Further optimize the models for faster processing.

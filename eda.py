import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mplcursors

# Define the path to your dataset
dataset_path = 'Data/train'

# Define the emotion classes
emotional_classes = ["ANGER", "CONTEMPT", "DISGUST", "FEAR", "HAPPINESS", "NEUTRAL", "SADNESS", "SURPRISE"]

# Create a dictionary to store images and labels for each emotion
emotion_data = {emotion: {'images': [], 'labels': []} for emotion in emotional_classes}

# Maximum number of images to load per class
max_images_per_class = 5

# Load the images and labels into the dictionary
for i, emotion in enumerate(emotional_classes):
    emotion_path = os.path.join(dataset_path, emotion)
    if not os.path.exists(emotion_path):
        print(f"Directory {emotion_path} does not exist.")
        continue
    image_files = os.listdir(emotion_path)[:max_images_per_class]  # Limit number of images loaded
    for img_name in image_files:
        img_path = os.path.join(emotion_path, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img = cv2.resize(img, (48, 48))  # Resize image to 48x48 for consistency and speed
            emotion_data[emotion]['images'].append(img)
            emotion_data[emotion]['labels'].append(emotion)  # Use emotion label instead of numerical label

# Plot the class distribution
def plot_class_distribution(dataset_path, emotional_classes):
    class_counts = {}
    for emotion in emotional_classes:
        class_path = os.path.join(dataset_path, emotion)
        images = os.listdir(class_path)
        class_counts[emotion] = len(images)
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(range(len(class_counts)), list(class_counts.values()), align='center', color='skyblue')
    plt.xticks(range(len(class_counts)), list(class_counts.keys()), rotation=45)
    plt.xlabel('Emotion Class', fontsize=12)
    plt.ylabel('Number of Images', fontsize=12)
    plt.title('Distribution of Images Across Emotion Classes', fontsize=14)

    # Add hover functionality to show counts
    mplcursors.cursor(bars, hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(f"Count: {class_counts[list(class_counts.keys())[sel.target.index]]}"))

# Plot a few images for each emotion with their labels
def plot_images_with_labels(emotion_data, emotional_classes):
    sns.set(style="whitegrid")
    num_images = 5
    fig, axes = plt.subplots(len(emotional_classes), num_images, figsize=(8, 8))

    for i, emotion in enumerate(emotional_classes):
        images = emotion_data[emotion]['images']
        labels = emotion_data[emotion]['labels']
        for j in range(num_images):
            if j < len(images):
                axes[i, j].imshow(images[j], cmap='gray')
                axes[i, j].set_title(f"{labels[j]}", fontsize=10)
            axes[i, j].axis('off')
            if j == 0:
                axes[i, j].set_ylabel(emotion, fontsize=12, rotation=0, labelpad=30)
    
    plt.tight_layout()

# Show both plots
plot_class_distribution(dataset_path, emotional_classes)
plot_images_with_labels(emotion_data, emotional_classes)
plt.show()


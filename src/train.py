import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# -----------------------------
# 1. Settings
# -----------------------------
IMG_SIZE = (128, 128)
BATCH_SIZE = 32
EPOCHS = 20


# -----------------------------
# 2. Load and preprocess data
# -----------------------------
datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=20,
    zoom_range=0.2,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)


# Training data
train_data = datagen.flow_from_directory(
    "dataset",
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="binary",
    subset="training"
)


# Validation data
validation_data = datagen.flow_from_directory(
    "dataset",
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="binary",
    subset="validation"
)


print("Class labels:", train_data.class_indices)


# -----------------------------
# 3. Build CNN Model
# -----------------------------
model = Sequential([

    # Convolutional Layer 1
    Conv2D(
        32,
        (3, 3),
        activation="relu",
        input_shape=(128, 128, 3)
    ),
    MaxPooling2D(2, 2),

    # Convolutional Layer 2
    Conv2D(
        64,
        (3, 3),
        activation="relu"
    ),
    MaxPooling2D(2, 2),

    # Convolutional Layer 3
    Conv2D(
        128,
        (3, 3),
        activation="relu"
    ),
    MaxPooling2D(2, 2),

    # Convert feature maps into one-dimensional vector
    Flatten(),

    # Fully Connected Layer
    Dense(
        128,
        activation="relu"
    ),

    # Prevent overfitting
    Dropout(0.5),

    # Output Layer
    Dense(
        1,
        activation="sigmoid"
    )
])


# -----------------------------
# 4. Compile Model
# -----------------------------
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# Display model architecture
model.summary()


# -----------------------------
# 5. Train Model
# -----------------------------
history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=EPOCHS
)


# -----------------------------
# 6. Plot Accuracy
# -----------------------------
plt.figure(figsize=(8, 5))

plt.plot(
    history.history["accuracy"],
    label="Training Accuracy"
)

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy"
)

plt.title("Training and Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)

plt.savefig("accuracy_graph.png")

plt.show()


# -----------------------------
# 7. Plot Loss
# -----------------------------
plt.figure(figsize=(8, 5))

plt.plot(
    history.history["loss"],
    label="Training Loss"
)

plt.plot(
    history.history["val_loss"],
    label="Validation Loss"
)

plt.title("Training and Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

plt.savefig("loss_graph.png")

plt.show()


# -----------------------------
# 8. Save Model
# -----------------------------
model.save("models/face_mask_cnn.keras")

print("Model saved successfully!")
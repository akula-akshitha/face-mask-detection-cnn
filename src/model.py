import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense, Dropout

# Create CNN model
model = Sequential([
    
    # First convolution block
    Conv2D(32, (3, 3), activation="relu", input_shape=(128, 128, 3)),
    MaxPooling2D(2, 2),

    # Second convolution block
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D(2, 2),

    # Third convolution block
    Conv2D(128, (3, 3), activation="relu"),
    MaxPooling2D(2, 2),

    # Convert feature maps into a vector
    Flatten(),

    # Fully connected layer
    Dense(128, activation="relu"),

    # Reduce overfitting
    Dropout(0.5),

    # Binary output
    Dense(1, activation="sigmoid")
])

# Compile model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Display architecture
model.summary()
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Image size
IMG_SIZE = (128, 128)

# Data augmentation + normalization for training
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=20,
    zoom_range=0.2,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

# Training data
train_data = train_datagen.flow_from_directory(
    "dataset",
    target_size=IMG_SIZE,
    batch_size=32,
    class_mode="binary",
    subset="training"
)

# Validation data
validation_data = train_datagen.flow_from_directory(
    "dataset",
    target_size=IMG_SIZE,
    batch_size=32,
    class_mode="binary",
    subset="validation"
)

print("Class labels:", train_data.class_indices)
print("Training images:", train_data.samples)
print("Validation images:", validation_data.samples)
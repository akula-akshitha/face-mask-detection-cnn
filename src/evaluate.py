import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


# -----------------------------
# 1. Settings
# -----------------------------
IMG_SIZE = (128, 128)
BATCH_SIZE = 32


# -----------------------------
# 2. Load trained model
# -----------------------------
model = load_model("models/face_mask_cnn.keras")

print("Model loaded successfully!")


# -----------------------------
# 3. Load validation dataset
# -----------------------------
datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2
)

validation_data = datagen.flow_from_directory(
    "dataset",
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="binary",
    subset="validation",
    shuffle=False
)

print("Class labels:", validation_data.class_indices)


# -----------------------------
# 4. Make predictions
# -----------------------------
predictions = model.predict(validation_data)

# Convert probabilities to 0 or 1
y_pred = (predictions > 0.5).astype(int).flatten()

# Actual labels
y_true = validation_data.classes


# -----------------------------
# 5. Calculate metrics
# -----------------------------
accuracy = accuracy_score(y_true, y_pred)

precision = precision_score(
    y_true,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_true,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_true,
    y_pred,
    zero_division=0
)


# -----------------------------
# 6. Display results
# -----------------------------
print("\n========== MODEL EVALUATION ==========")

print(f"Accuracy  : {accuracy * 100:.2f}%")
print(f"Precision : {precision * 100:.2f}%")
print(f"Recall    : {recall * 100:.2f}%")
print(f"F1-Score  : {f1 * 100:.2f}%")


# -----------------------------
# 7. Classification Report
# -----------------------------
print("\n========== CLASSIFICATION REPORT ==========")

print(
    classification_report(
        y_true,
        y_pred,
        target_names=["With Mask", "Without Mask"],
        zero_division=0
    )
)


# -----------------------------
# 8. Confusion Matrix
# -----------------------------
cm = confusion_matrix(y_true, y_pred)

print("\n========== CONFUSION MATRIX ==========")
print(cm)


# -----------------------------
# 9. Display Confusion Matrix
# -----------------------------
plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=["With Mask", "Without Mask"],
    yticklabels=["With Mask", "Without Mask"]
)

plt.title("Confusion Matrix - Face Mask Detection")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

plt.tight_layout()

plt.savefig("confusion_matrix.png")

plt.show()
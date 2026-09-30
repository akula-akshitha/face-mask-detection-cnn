from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
import cv2
import numpy as np
from pathlib import Path


# --------------------------------------------------
# FastAPI App
# --------------------------------------------------

app = FastAPI(title="Face Mask Detection API")


# --------------------------------------------------
# CORS - Allows React to communicate with FastAPI
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Load Your Trained CNN Model
# --------------------------------------------------

MODEL_PATH = Path(__file__).parent / "model" / "face_mask_cnn.keras"

model = load_model(MODEL_PATH)


# --------------------------------------------------
# OpenCV Face Detector
# --------------------------------------------------

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


# --------------------------------------------------
# Home Route
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Face Mask Detection API is running"
    }


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": "loaded"
    }


# --------------------------------------------------
# Prediction Route
# --------------------------------------------------

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Read uploaded image
    image_bytes = await file.read()

    # Convert bytes to OpenCV image
    image_array = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Check if image is valid
    if image is None:
        return {
            "success": False,
            "message": "Invalid image"
        }

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # No face found
    if len(faces) == 0:
        return {
            "success": False,
            "message": "No face detected"
        }

    results = []

    # Process every detected face
    for (x, y, w, h) in faces:

        # Crop face
        face = image[y:y+h, x:x+w]

        # Convert BGR to RGB
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

        # Resize to model input size
        face = cv2.resize(face, (128, 128))

        # Normalize
        face = face / 255.0

        # Add batch dimension
        face = np.expand_dims(face, axis=0)

        # CNN prediction
        prediction = model.predict(face, verbose=0)[0][0]

        # Your model:
        # 0 = with_mask
        # 1 = without_mask

        if prediction < 0.5:
            label = "MASK"
            confidence = (1 - prediction) * 100
        else:
            label = "NO MASK"
            confidence = prediction * 100

        results.append({
            "label": label,
            "confidence": round(float(confidence), 2),
            "box": {
                "x": int(x),
                "y": int(y),
                "width": int(w),
                "height": int(h)
            }
        })

    return {
        "success": True,
        "faces_detected": len(results),
        "results": results
    }
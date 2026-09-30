import cv2
import numpy as np
from tensorflow.keras.models import load_model


# --------------------------------
# 1. Load trained CNN model
# --------------------------------
model = load_model("models/face_mask_cnn.keras")

print("Model loaded successfully!")


# --------------------------------
# 2. Load OpenCV face detector
# --------------------------------
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if face_detector.empty():
    print("Error: Could not load face detector.")
    exit()


# --------------------------------
# 3. Start webcam
# --------------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


print("Webcam started!")
print("Press 'q' to quit.")


# --------------------------------
# 4. Real-time detection
# --------------------------------
while True:

    # Read frame from webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(60, 60)
    )

    # Process each detected face
    for (x, y, w, h) in faces:

        # Crop face
        face = frame[y:y+h, x:x+w]

        # Check that face is valid
        if face.size == 0:
            continue

        # Resize face to CNN input size
        face = cv2.resize(face, (128, 128))

        # Convert BGR to RGB
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

        # Normalize pixel values
        face = face.astype("float32") / 255.0

        # Add batch dimension
        face = np.expand_dims(face, axis=0)

        # Make prediction
        prediction = model.predict(face, verbose=0)[0][0]

        # --------------------------------
        # Class mapping
        # --------------------------------
        # 0 = With Mask
        # 1 = Without Mask

        if prediction < 0.5:
            label = "MASK"
            confidence = (1 - prediction) * 100
        else:
            label = "NO MASK"
            confidence = prediction * 100

        # --------------------------------
        # Draw bounding box
        # --------------------------------
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Text to display
        text = f"{label}: {confidence:.1f}%"

        # Display label
        cv2.putText(
            frame,
            text,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # --------------------------------
    # Display webcam frame
    # --------------------------------
    cv2.imshow(
        "Real-Time Face Mask Detection",
        frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# --------------------------------
# 5. Release resources
# --------------------------------
cap.release()
cv2.destroyAllWindows()

print("Webcam closed.")
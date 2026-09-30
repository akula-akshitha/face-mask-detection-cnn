# 😷 Face Mask Detection Using CNN

## 📌 Overview

This project is a real-time Face Mask Detection system developed using a Convolutional Neural Network (CNN).

The system detects faces and classifies them into two categories:

- 😷 With Mask
- ❌ Without Mask

It supports both image upload detection and real-time webcam detection.

---

## ✨ Features

- Image upload for mask detection
- Real-time webcam detection
- Face detection using OpenCV
- CNN-based classification
- Confidence score
- Bounding boxes around detected faces
- MASK / NO MASK classification
- Analytics page showing model performance

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Scikit-learn
- FastAPI
- React
- Vite
- JavaScript
- CSS

---

## 📊 Dataset

The model was trained using a dataset containing **7,553 images**.

| Class | Images |
|---|---:|
| With Mask | 3,725 |
| Without Mask | 3,828 |
| Total | 7,553 |

The dataset is not included in this repository.

---

## 🧠 CNN Model

The CNN contains:

- Conv2D – 32 filters
- MaxPooling
- Conv2D – 64 filters
- MaxPooling
- Conv2D – 128 filters
- MaxPooling
- Flatten
- Dense – 128 neurons
- Dropout – 0.5
- Sigmoid output

### Model Configuration

| Parameter | Value |
|---|---|
| Input Size | 128 × 128 × 3 |
| Optimizer | Adam |
| Loss | Binary Cross Entropy |
| Epochs | 20 |
| Batch Size | 32 |
| Classes | 2 |

---

## 📈 Results

| Metric | Score |
|---|---:|
| Accuracy | 94.44% |
| Precision | 97.89% |
| Recall | 90.98% |
| F1 Score | 94.31% |

### Confusion Matrix

```text
                 Predicted
                Mask   No Mask

Actual Mask      730      15

Actual No Mask    69     696
🏗️ System Architecture
User
  ↓
React Frontend
  ↓
FastAPI Backend
  ↓
OpenCV Face Detection
  ↓
CNN Model
  ↓
MASK / NO MASK
  ↓
Confidence + Bounding Box
📂 Project Structure
Face-Mask-Detection/
│
├── backend/
│   ├── main.py
│   └── model/
│       └── face_mask_cnn.keras
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── pages/
│       ├── App.jsx
│       ├── App.css
│       └── LiveCamera.jsx
│
├── src/
│   ├── train.py
│   ├── evaluate.py
│   ├── model.py
│   ├── preprocess.py
│   ├── plot_history.py
│   └── realtime.py
│
├── accuracy_graph.png
├── loss_graph.png
├── confusion_matrix.png
├── .gitignore
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/akula-akshitha/face-mask-detection-cnn.git
cd face-mask-detection-cnn
2. Create virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\Activate.ps1
3. Install backend dependencies
pip install tensorflow fastapi uvicorn python-multipart opencv-python numpy scikit-learn
4. Start the backend
cd backend
python -m uvicorn main:app --reload

Backend:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs
5. Start the frontend

Open another terminal:

cd frontend
npm install
npm run dev

Frontend:

http://localhost:5173
🚀 How It Works
Image Detection
User uploads an image.
OpenCV detects the face.
The face is resized to 128 × 128.
Pixel values are normalized.
The CNN predicts MASK or NO MASK.
The result and confidence are displayed.
Live Camera Detection
User allows camera access.
Webcam frames are captured.
OpenCV detects faces.
Each face is passed to the CNN.
The prediction is displayed with a bounding box.
🔮 Future Scope
Improve detection accuracy
Support different types of masks
Use larger and more diverse datasets
Improve real-time detection speed
Deploy the application online
Develop a mobile application
👩‍💻 Contributors
A. Akshitha

B.Tech – Computer Science and Engineering (AI & ML)

V. Likhitha

B.Tech – Computer Science and Engineering (AI & ML)
## License

This project is for **educational purposes** — college course-end project / semester-end Deep Learning Laboratory submission.

---

## 🙏 Acknowledgements

- **Dataset:** [Face Mask Detection Dataset – Kaggle](https://www.kaggle.com/)
- **Deep Learning Framework:** TensorFlow and Keras
- **Computer Vision:** OpenCV
- **Backend:** FastAPI
- **Frontend:** React and Vite
- **Machine Learning Tools:** NumPy and scikit-learn
- **Inspiration:** Deep learning and computer vision approaches for automated face mask detection


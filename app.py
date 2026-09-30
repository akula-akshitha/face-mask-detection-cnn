import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
import os

from PIL import Image


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="FaceGuard AI",
    page_icon="😷",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Remove top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Hero */
    .hero {
        background: linear-gradient(
            135deg,
            #111827,
            #1e3a8a
        );
        padding: 45px;
        border-radius: 24px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.12);
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 10px;
        font-weight: 800;
    }

    .hero p {
        font-size: 18px;
        opacity: 0.9;
        margin-bottom: 0;
    }

    .badge {
        display: inline-block;
        padding: 7px 15px;
        border-radius: 30px;
        background-color: rgba(255,255,255,0.15);
        margin-bottom: 18px;
        font-size: 14px;
        font-weight: 600;
    }

    /* Section titles */
    .section-title {
        font-size: 27px;
        font-weight: 750;
        color: #111827;
        margin-top: 25px;
        margin-bottom: 18px;
    }

    .section-subtitle {
        color: #6b7280;
        font-size: 15px;
        margin-bottom: 20px;
    }

    /* Metric cards */
    .metric-card {
        background: white;
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 5px 18px rgba(0,0,0,0.06);
        text-align: center;
        min-height: 125px;
    }

    .metric-title {
        color: #6b7280;
        font-size: 14px;
        font-weight: 600;
    }

    .metric-value {
        color: #111827;
        font-size: 30px;
        font-weight: 800;
        margin-top: 8px;
    }

    /* Result cards */
    .mask-result {
        background: #ecfdf5;
        border: 2px solid #10b981;
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        margin-top: 20px;
    }

    .no-mask-result {
        background: #fef2f2;
        border: 2px solid #ef4444;
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        margin-top: 20px;
    }

    .result-title {
        font-size: 28px;
        font-weight: 800;
    }

    .result-confidence {
        font-size: 17px;
        margin-top: 8px;
    }

    /* Info cards */
    .info-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 25px;
        box-shadow: 0 5px 18px rgba(0,0,0,0.05);
        height: 100%;
    }

    .info-card h3 {
        color: #111827;
        margin-bottom: 15px;
    }

    .info-card p {
        color: #6b7280;
        line-height: 1.7;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6b7280;
        padding: 30px;
        font-size: 14px;
    }

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background-color: transparent !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_cnn_model():

    return tf.keras.models.load_model(
        "models/face_mask_cnn.keras"
    )


model = load_cnn_model()


# =========================================================
# LOAD FACE DETECTOR
# =========================================================

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades
    + "haarcascade_frontalface_default.xml"
)


# =========================================================
# PREDICTION FUNCTION
# =========================================================

def predict_face(face):

    face = cv2.resize(
        face,
        (128, 128)
    )

    face = cv2.cvtColor(
        face,
        cv2.COLOR_BGR2RGB
    )

    face = face.astype("float32") / 255.0

    face = np.expand_dims(
        face,
        axis=0
    )

    prediction = model.predict(
        face,
        verbose=0
    )[0][0]

    if prediction < 0.5:

        label = "MASK"
        confidence = (1 - prediction) * 100

    else:

        label = "NO MASK"
        confidence = prediction * 100

    return label, confidence


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center; padding:20px 0;">

        <div style="font-size:55px;">
        😷
        </div>

        <h2 style="margin-bottom:0;">
        FaceGuard AI
        </h2>

        <p style="color:#9ca3af;">
        Intelligent Mask Detection
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### 🔍 Detection Mode")

    mode = st.radio(
        "Choose how you want to test the model",
        [
            "📷 Image Detection",
            "🎥 Camera Detection"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("### 🧠 AI Model")

    st.write("**Architecture:** CNN")
    st.write("**Input:** 128 × 128 × 3")
    st.write("**Classes:** 2")
    st.write("**Epochs:** 20")

    st.markdown("---")

    st.caption(
        "Deep Learning Course-End Project"
    )


# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    """
    <div class="hero">

        <div class="badge">
        🧠 POWERED BY CONVOLUTIONAL NEURAL NETWORK
        </div>

        <h1>
        😷 FaceGuard AI
        </h1>

        <p>
        Real-Time Face Mask Detection using Deep Learning
        </p>

        <p style="margin-top:12px;">
        Detect whether a person is wearing a protective
        face mask using our trained CNN model.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PERFORMANCE METRICS
# =========================================================

st.markdown(
    '<div class="section-title">📊 Model Performance</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Performance of the trained CNN model on the validation dataset.</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">ACCURACY</div>
            <div class="metric-value">94.44%</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">PRECISION</div>
            <div class="metric-value">97.89%</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">RECALL</div>
            <div class="metric-value">90.98%</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">F1-SCORE</div>
            <div class="metric-value">94.31%</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# DETECTION SECTION
# =========================================================

st.markdown(
    '<div class="section-title">🔎 Detection Center</div>',
    unsafe_allow_html=True
)


# =========================================================
# IMAGE DETECTION
# =========================================================

if mode == "📷 Image Detection":

    st.markdown(
        '<div class="section-subtitle">Upload an image containing one or more faces.</div>',
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )

    if uploaded_file:

        image = Image.open(
            uploaded_file
        ).convert("RGB")

        frame = np.array(image)

        frame_bgr = cv2.cvtColor(
            frame,
            cv2.COLOR_RGB2BGR
        )

        gray = cv2.cvtColor(
            frame_bgr,
            cv2.COLOR_BGR2GRAY
        )

        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        if len(faces) == 0:

            st.warning(
                "⚠️ No face detected. Please upload a clear face image."
            )

            st.image(
                image,
                caption="Uploaded Image",
                use_container_width=True
            )

        else:

            st.info(
                f"👤 {len(faces)} face(s) detected"
            )

            results = []

            for (x, y, w, h) in faces:

                face = frame_bgr[
                    y:y+h,
                    x:x+w
                ]

                label, confidence = predict_face(
                    face
                )

                results.append(
                    (label, confidence)
                )

                if label == "MASK":

                    box_color = (
                        0,
                        200,
                        100
                    )

                else:

                    box_color = (
                        0,
                        0,
                        255
                    )

                cv2.rectangle(
                    frame_bgr,
                    (x, y),
                    (x+w, y+h),
                    box_color,
                    3
                )

                text = (
                    f"{label} "
                    f"{confidence:.1f}%"
                )

                cv2.putText(
                    frame_bgr,
                    text,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    box_color,
                    2
                )

            result_image = cv2.cvtColor(
                frame_bgr,
                cv2.COLOR_BGR2RGB
            )

            st.image(
                result_image,
                caption="Detection Result",
                use_container_width=True
            )

            # Results
            st.markdown(
                '<div class="section-title">🎯 Detection Results</div>',
                unsafe_allow_html=True
            )

            result_columns = st.columns(
                len(results)
            )

            for i, result in enumerate(results):

                label, confidence = result

                with result_columns[i]:

                    if label == "MASK":

                        st.markdown(
                            f"""
                            <div class="mask-result">

                                <div class="result-title">
                                😷 MASK
                                </div>

                                <div class="result-confidence">
                                Confidence:
                                <b>{confidence:.2f}%</b>
                                </div>

                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    else:

                        st.markdown(
                            f"""
                            <div class="no-mask-result">

                                <div class="result-title">
                                🚫 NO MASK
                                </div>

                                <div class="result-confidence">
                                Confidence:
                                <b>{confidence:.2f}%</b>
                                </div>

                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    st.progress(
                        int(min(confidence, 100))
                    )


# =========================================================
# CAMERA DETECTION
# =========================================================

else:

    st.markdown(
        '<div class="section-subtitle">Capture an image using your webcam and let the CNN analyze it.</div>',
        unsafe_allow_html=True
    )

    camera_image = st.camera_input(
        "📸 Capture Image"
    )

    if camera_image:

        image = Image.open(
            camera_image
        ).convert("RGB")

        frame = np.array(image)

        frame_bgr = cv2.cvtColor(
            frame,
            cv2.COLOR_RGB2BGR
        )

        gray = cv2.cvtColor(
            frame_bgr,
            cv2.COLOR_BGR2GRAY
        )

        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        if len(faces) == 0:

            st.warning(
                "⚠️ No face detected. Please position your face clearly."
            )

            st.image(
                image,
                caption="Captured Image",
                use_container_width=True
            )

        else:

            results = []

            for (x, y, w, h) in faces:

                face = frame_bgr[
                    y:y+h,
                    x:x+w
                ]

                label, confidence = predict_face(
                    face
                )

                results.append(
                    (label, confidence)
                )

                if label == "MASK":

                    box_color = (
                        0,
                        200,
                        100
                    )

                else:

                    box_color = (
                        0,
                        0,
                        255
                    )

                cv2.rectangle(
                    frame_bgr,
                    (x, y),
                    (x+w, y+h),
                    box_color,
                    3
                )

                text = (
                    f"{label}: "
                    f"{confidence:.1f}%"
                )

                cv2.putText(
                    frame_bgr,
                    text,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    box_color,
                    2
                )

            result_image = cv2.cvtColor(
                frame_bgr,
                cv2.COLOR_BGR2RGB
            )

            st.image(
                result_image,
                caption="Camera Detection Result",
                use_container_width=True
            )

            for label, confidence in results:

                if label == "MASK":

                    st.success(
                        f"😷 MASK DETECTED — {confidence:.2f}% confidence"
                    )

                else:

                    st.error(
                        f"🚫 NO MASK DETECTED — {confidence:.2f}% confidence"
                    )

                st.progress(
                    int(min(confidence, 100))
                )


# =========================================================
# MODEL DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">🧠 About the AI Model</div>',
    unsafe_allow_html=True
)


info1, info2 = st.columns(2)


with info1:

    st.markdown(
        """
        <div class="info-card">

        <h3>🔬 CNN Architecture</h3>

        <p>
        Our face mask detector uses a Convolutional Neural
        Network designed to extract visual features from
        face images.
        </p>

        <p>
        <b>Architecture:</b>
        </p>

        <p>
        Conv2D (32) → MaxPooling →
        Conv2D (64) → MaxPooling →
        Conv2D (128) → MaxPooling →
        Flatten → Dense (128) →
        Dropout → Sigmoid
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with info2:

    st.markdown(
        """
        <div class="info-card">

        <h3>⚙️ Training Configuration</h3>

        <p>
        <b>Input Size:</b> 128 × 128 × 3
        </p>

        <p>
        <b>Optimizer:</b> Adam
        </p>

        <p>
        <b>Loss:</b> Binary Crossentropy
        </p>

        <p>
        <b>Training Epochs:</b> 20
        </p>

        <p>
        <b>Classes:</b> With Mask / Without Mask
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# GRAPHS
# =========================================================

st.markdown(
    '<div class="section-title">📈 Training Analysis</div>',
    unsafe_allow_html=True
)


graph1, graph2 = st.columns(2)


with graph1:

    if os.path.exists(
        "accuracy_graph.png"
    ):

        st.image(
            "accuracy_graph.png",
            caption="Training vs Validation Accuracy",
            use_container_width=True
        )


with graph2:

    if os.path.exists(
        "loss_graph.png"
    ):

        st.image(
            "loss_graph.png",
            caption="Training vs Validation Loss",
            use_container_width=True
        )


# =========================================================
# CONFUSION MATRIX
# =========================================================

if os.path.exists(
    "confusion_matrix.png"
):

    st.markdown(
        '<div class="section-title">🔥 Confusion Matrix</div>',
        unsafe_allow_html=True
    )

    st.image(
        "confusion_matrix.png",
        caption="CNN Classification Performance",
        width=650
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

    😷 <b>FaceGuard AI</b>

    <br>

    Real-Time Face Mask Detection using Convolutional Neural Networks

    <br><br>

    Deep Learning Course-End Project

    </div>
    """,
    unsafe_allow_html=True
)
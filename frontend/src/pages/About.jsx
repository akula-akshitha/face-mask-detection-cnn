function About() {
  return (
    <div className="page-container">

      {/* Header */}
      <section className="page-header">
        <p className="section-tag">ABOUT THE PROJECT</p>

        <h1>Real-Time Face Mask Detection</h1>

        <p>
          An AI-powered computer vision system designed to detect
          whether people are wearing face masks using a
          Convolutional Neural Network.
        </p>
      </section>

      {/* Project Overview */}
      <section className="about-section">

        <div className="about-content">

          <p className="section-tag">PROJECT OVERVIEW</p>

          <h2>Computer Vision Meets Deep Learning</h2>

          <p>
            Face mask detection is a computer vision application
            that can be used in public spaces, healthcare
            environments, educational institutions and other
            areas where mask compliance may be important.
          </p>

          <p>
            This project uses a Convolutional Neural Network (CNN)
            trained on thousands of face images to classify faces
            into two categories:
          </p>

          <div className="class-list">

            <div className="class-item">
              <span>😷</span>
              <div>
                <strong>With Mask</strong>
                <p>Face detected with a mask.</p>
              </div>
            </div>

            <div className="class-item">
              <span>👤</span>
              <div>
                <strong>Without Mask</strong>
                <p>Face detected without a mask.</p>
              </div>
            </div>

          </div>

        </div>

      </section>

      {/* Technology */}
      <section className="about-section">

        <div className="analytics-title">

          <p className="section-tag">TECHNOLOGY STACK</p>

          <h2>Technologies Used</h2>

          <p>
            The project combines deep learning, computer vision
            and modern web development technologies.
          </p>

        </div>

        <div className="technology-grid">

          <div className="technology-card">
            <div className="technology-icon">🧠</div>
            <h3>TensorFlow / Keras</h3>
            <p>
              Used to build, train and deploy the CNN model.
            </p>
          </div>

          <div className="technology-card">
            <div className="technology-icon">👁️</div>
            <h3>OpenCV</h3>
            <p>
              Used for face detection and real-time camera
              processing.
            </p>
          </div>

          <div className="technology-card">
            <div className="technology-icon">⚛️</div>
            <h3>React</h3>
            <p>
              Provides the interactive frontend and user
              interface.
            </p>
          </div>

          <div className="technology-card">
            <div className="technology-icon">⚡</div>
            <h3>FastAPI</h3>
            <p>
              Provides the backend API for model predictions.
            </p>
          </div>

          <div className="technology-card">
            <div className="technology-icon">🐍</div>
            <h3>Python</h3>
            <p>
              Used for machine learning, image processing and
              backend development.
            </p>
          </div>

          <div className="technology-card">
            <div className="technology-icon">📊</div>
            <h3>NumPy & Scikit-learn</h3>
            <p>
              Used for numerical processing and model
              evaluation.
            </p>
          </div>

        </div>

      </section>

      {/* How Model Works */}
      <section className="about-section">

        <div className="analytics-title">

          <p className="section-tag">WORKFLOW</p>

          <h2>How The System Works</h2>

        </div>

        <div className="workflow-grid">

          <div className="workflow-card">
            <span>01</span>
            <h3>Input Image</h3>
            <p>
              An image is uploaded or captured through the
              webcam.
            </p>
          </div>

          <div className="workflow-card">
            <span>02</span>
            <h3>Face Detection</h3>
            <p>
              OpenCV identifies faces present in the image.
            </p>
          </div>

          <div className="workflow-card">
            <span>03</span>
            <h3>CNN Classification</h3>
            <p>
              The detected face is resized to 128 × 128 pixels
              and passed to the trained CNN.
            </p>
          </div>

          <div className="workflow-card">
            <span>04</span>
            <h3>Prediction</h3>
            <p>
              The model predicts MASK or NO MASK with a
              confidence score.
            </p>
          </div>

        </div>

      </section>

      {/* Project Results */}
      <section className="about-section">

        <div className="analytics-title">

          <p className="section-tag">MODEL RESULTS</p>

          <h2>Performance</h2>

        </div>

        <div className="about-stats">

          <div>
            <strong>94.44%</strong>
            <span>Accuracy</span>
          </div>

          <div>
            <strong>97.89%</strong>
            <span>Precision</span>
          </div>

          <div>
            <strong>90.98%</strong>
            <span>Recall</span>
          </div>

          <div>
            <strong>94.31%</strong>
            <span>F1 Score</span>
          </div>

        </div>

      </section>

      {/* Future Scope */}
      <section className="about-section future-section">

        <p className="section-tag">FUTURE SCOPE</p>

        <h2>Future Improvements</h2>

        <ul>
          <li>Multi-person real-time detection</li>
          <li>Improved face detection using modern object detection models</li>
          <li>Deployment on edge devices and CCTV systems</li>
          <li>Cloud-based monitoring and analytics</li>
          <li>Real-time alerts for mask violations</li>
        </ul>

      </section>

    </div>
  );
}

export default About;
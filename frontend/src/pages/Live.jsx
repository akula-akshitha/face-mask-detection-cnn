import LiveCamera from "../LiveCamera";

function Live() {
  return (
    <div className="page-container">

      <section className="page-header">
        <p className="section-tag">
          REAL-TIME AI DETECTION
        </p>

        <h1>Live Camera Detection</h1>

        <p>
          Use your webcam to detect face masks in real time
          using our CNN model.
        </p>
      </section>

      <section className="live-page-section">

        <div className="live-info">

          <div className="live-status">
            <span className="status-dot"></span>
            CAMERA SYSTEM READY
          </div>

          <h2>
            Real-Time Face Mask Detection
          </h2>

          <p>
            Start your webcam and our AI system will detect
            faces and classify them as MASK or NO MASK.
          </p>

          <div className="live-features">

            <div className="live-feature">
              <span>✓</span>
              Real-time face detection
            </div>

            <div className="live-feature">
              <span>✓</span>
              CNN classification
            </div>

            <div className="live-feature">
              <span>✓</span>
              Confidence score
            </div>

            <div className="live-feature">
              <span>✓</span>
              Bounding boxes
            </div>

          </div>

        </div>

        <div className="live-camera-wrapper">
          <LiveCamera />
        </div>

      </section>

    </div>
  );
}

export default Live;
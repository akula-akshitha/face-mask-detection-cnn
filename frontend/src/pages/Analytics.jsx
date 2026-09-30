function Analytics() {
  return (
    <div className="page-container">

      {/* Header */}
      <section className="page-header">
        <p className="section-tag">MODEL PERFORMANCE</p>

        <h1>Model Analytics</h1>

        <p>
          Performance evaluation of our Convolutional Neural
          Network trained for face mask detection.
        </p>
      </section>

      {/* Metrics */}
      <section className="analytics-metrics">

        <div className="metric-card">
          <span>Accuracy</span>
          <strong>94.44%</strong>
          <small>Overall correctness</small>
        </div>

        <div className="metric-card">
          <span>Precision</span>
          <strong>97.89%</strong>
          <small>Prediction precision</small>
        </div>

        <div className="metric-card">
          <span>Recall</span>
          <strong>90.98%</strong>
          <small>Detection sensitivity</small>
        </div>

        <div className="metric-card">
          <span>F1 Score</span>
          <strong>94.31%</strong>
          <small>Balanced performance</small>
        </div>

      </section>

      {/* Training Graphs */}
      <section className="analytics-section">

        <div className="analytics-title">
          <p className="section-tag">TRAINING ANALYSIS</p>

          <h2>Training Performance</h2>

          <p>
            Training and validation performance across 20 epochs.
          </p>
        </div>

        <div className="graph-grid">

          <div className="graph-card">
            <h3>Accuracy Graph</h3>

            <img
              src="/accuracy_graph.png"
              alt="Training and validation accuracy graph"
            />
          </div>

          <div className="graph-card">
            <h3>Loss Graph</h3>

            <img
              src="/loss_graph.png"
              alt="Training and validation loss graph"
            />
          </div>

        </div>

      </section>

      {/* Confusion Matrix */}
      <section className="analytics-section">

        <div className="analytics-title">
          <p className="section-tag">CLASSIFICATION ANALYSIS</p>

          <h2>Confusion Matrix</h2>

          <p>
            The confusion matrix shows how accurately the model
            classified masked and unmasked faces.
          </p>
        </div>

        <div className="confusion-card">

          <div className="matrix">

            <div className="matrix-empty"></div>

            <div className="matrix-heading">
              Predicted Mask
            </div>

            <div className="matrix-heading">
              Predicted No Mask
            </div>

            <div className="matrix-heading vertical">
              Actual Mask
            </div>

            <div className="matrix-value correct">
              730
            </div>

            <div className="matrix-value incorrect">
              15
            </div>

            <div className="matrix-heading vertical">
              Actual No Mask
            </div>

            <div className="matrix-value incorrect">
              69
            </div>

            <div className="matrix-value correct">
              696
            </div>

          </div>

          <div className="matrix-summary">

            <div>
              <strong>730</strong>
              <span>Correct Mask</span>
            </div>

            <div>
              <strong>696</strong>
              <span>Correct No Mask</span>
            </div>

            <div>
              <strong>15</strong>
              <span>False Negative</span>
            </div>

            <div>
              <strong>69</strong>
              <span>False Positive</span>
            </div>

          </div>

        </div>

      </section>

      {/* Model Details */}
      <section className="analytics-section">

        <div className="analytics-title">
          <p className="section-tag">MODEL CONFIGURATION</p>

          <h2>Training Configuration</h2>
        </div>

        <div className="config-grid">

          <div className="config-card">
            <span>Architecture</span>
            <strong>Convolutional Neural Network</strong>
          </div>

          <div className="config-card">
            <span>Input Size</span>
            <strong>128 × 128 × 3</strong>
          </div>

          <div className="config-card">
            <span>Optimizer</span>
            <strong>Adam</strong>
          </div>

          <div className="config-card">
            <span>Loss Function</span>
            <strong>Binary Cross Entropy</strong>
          </div>

          <div className="config-card">
            <span>Epochs</span>
            <strong>20</strong>
          </div>

          <div className="config-card">
            <span>Classes</span>
            <strong>Mask / No Mask</strong>
          </div>

        </div>

      </section>

    </div>
  );
}

export default Analytics;
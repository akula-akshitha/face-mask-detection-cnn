import { useState } from "react";

function Detect() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (!file) return;

    setSelectedFile(file);
    setPreview(URL.createObjectURL(file));
    setResult(null);
  };

  const detectMask = async () => {
    if (!selectedFile) {
      alert("Please select an image first.");
      return;
    }

    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/predict",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error("Detection failed");
      }

      setResult(data);
    } catch (error) {
      console.error(error);

      setResult({
        success: false,
        message: "Unable to connect to the backend.",
      });
    }

    setLoading(false);
  };

  return (
    <div className="page-container">

      <section className="page-header">
        <p className="section-tag">AI IMAGE ANALYSIS</p>

        <h1>Face Mask Detection</h1>

        <p>
          Upload an image and let our CNN model detect whether
          a face is wearing a mask.
        </p>
      </section>

      <section className="detect-section">

        {/* Upload Card */}
        <div className="upload-card">

          <div className="upload-icon">
            📷
          </div>

          <h2>Upload Image</h2>

          <p>
            Select a JPG, JPEG or PNG image containing a face.
          </p>

          <label className="upload-button">
            Choose Image

            <input
              type="file"
              accept="image/*"
              onChange={handleFileChange}
              hidden
            />
          </label>

          {selectedFile && (
            <p className="file-name">
              Selected: {selectedFile.name}
            </p>
          )}

        </div>

        {/* Preview Card */}
        {preview && (
          <div className="preview-card">

            <h2>Image Preview</h2>

            <img
              src={preview}
              alt="Selected face"
              className="preview-image"
            />

            <button
              className="detect-button"
              onClick={detectMask}
              disabled={loading}
            >
              {loading ? "Analyzing..." : "Detect Mask"}
            </button>

          </div>
        )}

        {/* Result */}
        {result && (
          <div className="result-card">

            {result.success ? (
              <>
                <div className="result-header">
                  <h2>Detection Result</h2>
                  <span className="success-badge">
                    ✓ Detection Complete
                  </span>
                </div>

                {result.results.map((item, index) => (
                  <div
                    className="result-item"
                    key={index}
                  >
                    <div>
                      <p className="result-label">
                        Face {index + 1}
                      </p>

                      <h3
                        className={
                          item.label === "MASK"
                            ? "mask-result"
                            : "no-mask-result"
                        }
                      >
                        {item.label}
                      </h3>
                    </div>

                    <div className="confidence">
                      <span>Confidence</span>
                      <strong>
                        {item.confidence}%
                      </strong>
                    </div>
                  </div>
                ))}

                <div className="faces-count">
                  Faces detected:{" "}
                  <strong>{result.faces_detected}</strong>
                </div>
              </>
            ) : (
              <div className="error-result">
                <h2>Detection Failed</h2>

                <p>
                  {result.message}
                </p>
              </div>
            )}

          </div>
        )}

      </section>

    </div>
  );
}

export default Detect;
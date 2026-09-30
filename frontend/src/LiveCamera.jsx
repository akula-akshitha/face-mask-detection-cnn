import { useEffect, useRef, useState } from "react";

function LiveCamera() {
  const videoRef = useRef(null);
  const captureCanvasRef = useRef(null);
  const overlayCanvasRef = useRef(null);

  const streamRef = useRef(null);
  const intervalRef = useRef(null);

  const [cameraOn, setCameraOn] = useState(false);
  const [status, setStatus] = useState("Camera is stopped");
  const [error, setError] = useState("");
  const [result, setResult] = useState(null);

  // -----------------------------
  // START CAMERA
  // -----------------------------
  const startCamera = async () => {
    setError("");
    setResult(null);
    setStatus("Requesting camera permission...");

    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
        audio: false,
      });

      streamRef.current = stream;

      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        await videoRef.current.play();
      }

      setCameraOn(true);
      setStatus("Camera is running");

      intervalRef.current = setInterval(() => {
        detectFrame();
      }, 1000);

    } catch (err) {
      console.error("CAMERA ERROR:", err);

      setCameraOn(false);
      setStatus("Camera failed");

      setError(
        `${err.name || "Error"}: ${
          err.message || "Unable to access camera"
        }`
      );
    }
  };

  // -----------------------------
  // STOP CAMERA
  // -----------------------------
  const stopCamera = () => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
    }

    if (streamRef.current) {
      streamRef.current.getTracks().forEach((track) => {
        track.stop();
      });

      streamRef.current = null;
    }

    if (videoRef.current) {
      videoRef.current.srcObject = null;
    }

    clearOverlay();

    setCameraOn(false);
    setStatus("Camera is stopped");
    setResult(null);
  };

  // -----------------------------
  // CLEAR OVERLAY
  // -----------------------------
  const clearOverlay = () => {
    const canvas = overlayCanvasRef.current;

    if (!canvas) return;

    const ctx = canvas.getContext("2d");

    ctx.clearRect(
      0,
      0,
      canvas.width,
      canvas.height
    );
  };

  // -----------------------------
  // DRAW BOUNDING BOXES
  // -----------------------------
  const drawBoxes = (results) => {
    const video = videoRef.current;
    const canvas = overlayCanvasRef.current;

    if (!video || !canvas) return;

    const ctx = canvas.getContext("2d");

    const videoWidth = video.videoWidth;
    const videoHeight = video.videoHeight;

    if (!videoWidth || !videoHeight) return;

    canvas.width = videoWidth;
    canvas.height = videoHeight;

    ctx.clearRect(
      0,
      0,
      canvas.width,
      canvas.height
    );

    results.forEach((item) => {
      const {
        x,
        y,
        width,
        height
      } = item.box;

      const isMask = item.label === "MASK";

      const boxColor = isMask
        ? "#22c55e"
        : "#ef4444";

      // -----------------------------
      // BOX
      // -----------------------------

      ctx.strokeStyle = boxColor;
      ctx.lineWidth = 4;

      ctx.strokeRect(
        x,
        y,
        width,
        height
      );

      // -----------------------------
      // LABEL
      // -----------------------------

      const label =
        `${item.label} ${item.confidence}%`;

      ctx.font = "bold 18px Arial";

      const textWidth =
        ctx.measureText(label).width;

      const labelHeight = 30;

      const labelY =
        y > labelHeight
          ? y - labelHeight
          : y;

      ctx.fillStyle = boxColor;

      ctx.fillRect(
        x,
        labelY,
        textWidth + 16,
        labelHeight
      );

      ctx.fillStyle = "#ffffff";

      ctx.fillText(
        label,
        x + 8,
        labelY + 21
      );
    });
  };

  // -----------------------------
  // SEND FRAME TO BACKEND
  // -----------------------------
  const detectFrame = async () => {
    const video = videoRef.current;
    const canvas = captureCanvasRef.current;

    if (!video || !canvas) return;

    if (video.readyState < 2) return;

    const width = video.videoWidth;
    const height = video.videoHeight;

    if (!width || !height) return;

    canvas.width = width;
    canvas.height = height;

    const ctx = canvas.getContext("2d");

    ctx.drawImage(
      video,
      0,
      0,
      width,
      height
    );

    canvas.toBlob(async (blob) => {
      if (!blob) return;

      const formData = new FormData();

      formData.append(
        "file",
        blob,
        "camera.jpg"
      );

      try {
        const response = await fetch(
          "http://127.0.0.1:8000/predict",
          {
            method: "POST",
            body: formData,
          }
        );

        const data = await response.json();

        console.log("Prediction:", data);

        if (data.success) {
          setResult(data);

          drawBoxes(data.results);
        } else {
          setResult(null);

          clearOverlay();
        }

      } catch (err) {
        console.error(
          "Backend detection error:",
          err
        );
      }
    }, "image/jpeg");
  };

  // -----------------------------
  // CLEANUP
  // -----------------------------
  useEffect(() => {
    return () => {
      stopCamera();
    };
  }, []);

  // -----------------------------
  // CALCULATE STATISTICS
  // -----------------------------

  const totalFaces =
    result?.faces_detected || 0;

  const maskCount =
    result?.results?.filter(
      (item) => item.label === "MASK"
    ).length || 0;

  const noMaskCount =
    result?.results?.filter(
      (item) => item.label === "NO MASK"
    ).length || 0;

  const latestDetection =
    result?.results?.[0];

  // -----------------------------
  // UI
  // -----------------------------

  return (
    <div className="camera-container">

      {/* CAMERA */}

      <div className="camera-view">

        <video
          ref={videoRef}
          className="camera-video"
          autoPlay
          muted
          playsInline
        />

        <canvas
          ref={overlayCanvasRef}
          className="detection-canvas"
        />

        {!cameraOn && (
          <div
            style={{
              position: "absolute",
              inset: 0,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              color: "#94a3b8",
              fontSize: "18px",
              background: "#020817",
              zIndex: 2,
            }}
          >
            Camera is stopped
          </div>
        )}

      </div>

      {/* HIDDEN CAPTURE CANVAS */}

      <canvas
        ref={captureCanvasRef}
        style={{ display: "none" }}
      />

      {/* CONTROLS */}

      <div className="camera-controls">

        <button
          onClick={startCamera}
          disabled={cameraOn}
        >
          {cameraOn
            ? "Camera Running"
            : "Start Camera"}
        </button>

        <button
          onClick={stopCamera}
          disabled={!cameraOn}
        >
          Stop Camera
        </button>

      </div>

      {/* STATUS */}

      <div className="camera-result">

        <div className="camera-live-status">
          <span
            className={
              cameraOn
                ? "camera-status-dot active"
                : "camera-status-dot"
            }
          ></span>

          <span>
            {cameraOn
              ? "LIVE DETECTION ACTIVE"
              : "CAMERA OFFLINE"}
          </span>
        </div>

        <p className="camera-status-text">
          {status}
        </p>

        {/* ERROR */}

        {error && (
          <div className="camera-error">
            <strong>Camera Error</strong>

            <br />

            {error}
          </div>
        )}

      </div>

      {/* DETECTION DASHBOARD */}

      {cameraOn && (
        <div className="live-dashboard">

          {/* TOTAL FACES */}

          <div className="live-stat-card">

            <span className="live-stat-icon">
              👥
            </span>

            <div>
              <span className="live-stat-title">
                Faces Detected
              </span>

              <strong>
                {totalFaces}
              </strong>
            </div>

          </div>

          {/* MASK */}

          <div className="live-stat-card mask-card">

            <span className="live-stat-icon">
              😷
            </span>

            <div>
              <span className="live-stat-title">
                With Mask
              </span>

              <strong>
                {maskCount}
              </strong>
            </div>

          </div>

          {/* NO MASK */}

          <div className="live-stat-card no-mask-card">

            <span className="live-stat-icon">
              🚫
            </span>

            <div>
              <span className="live-stat-title">
                No Mask
              </span>

              <strong>
                {noMaskCount}
              </strong>
            </div>

          </div>

        </div>
      )}

      {/* LATEST DETECTION */}

      {latestDetection && (
        <div className="latest-detection">

          <div className="latest-detection-header">

            <span>
              LATEST DETECTION
            </span>

            <span className="detection-time">
              LIVE
            </span>

          </div>

          <div className="latest-detection-content">

            <div
              className={
                latestDetection.label === "MASK"
                  ? "detection-icon mask-icon"
                  : "detection-icon no-mask-icon"
              }
            >
              {latestDetection.label === "MASK"
                ? "😷"
                : "🚫"}
            </div>

            <div className="latest-info">

              <span>
                Detection Result
              </span>

              <strong
                className={
                  latestDetection.label === "MASK"
                    ? "mask-text"
                    : "no-mask-text"
                }
              >
                {latestDetection.label}
              </strong>

            </div>

            <div className="latest-confidence">

              <span>
                Confidence
              </span>

              <strong>
                {latestDetection.confidence}%
              </strong>

            </div>

          </div>

        </div>
      )}

    </div>
  );
}

export default LiveCamera;
import { BrowserRouter, Routes, Route, NavLink, Link } from "react-router-dom";

import Detect from "./pages/Detect";
import Live from "./pages/Live";
import Analytics from "./pages/Analytics";
import About from "./pages/About";

import "./App.css";


function Home() {
  return (
    <div className="home-page">

      {/* Hero */}
      <section className="hero">

        <div className="hero-content">

          <p className="section-tag">
            AI-POWERED COMPUTER VISION
          </p>

          <h1>
            Real-Time
            <br />
            <span>Face Mask Detection</span>
          </h1>

          <p className="hero-description">
            Detect face masks instantly using a Convolutional
            Neural Network combined with real-time computer vision.
          </p>

          <div className="hero-buttons">

            <Link to="/detect" className="primary-button">
              Try Image Detection →
            </Link>

            <Link to="/live" className="secondary-button">
              Live Camera
            </Link>

          </div>

        </div>

      </section>


      {/* Stats */}
      <section className="stats-section">

        <div className="stat-card">
          <strong>94.44%</strong>
          <span>Accuracy</span>
        </div>

        <div className="stat-card">
          <strong>97.89%</strong>
          <span>Precision</span>
        </div>

        <div className="stat-card">
          <strong>90.98%</strong>
          <span>Recall</span>
        </div>

        <div className="stat-card">
          <strong>94.31%</strong>
          <span>F1 Score</span>
        </div>

      </section>


      {/* Features */}
      <section className="home-section">

        <div className="section-heading">

          <p className="section-tag">
            WHAT THE SYSTEM DOES
          </p>

          <h2>
            Intelligent Mask Detection
          </h2>

          <p>
            Our system combines deep learning and computer vision
            to provide fast and reliable face mask detection.
          </p>

        </div>


        <div className="feature-grid">

          <div className="feature-card">

            <div className="feature-icon">
              📷
            </div>

            <h3>
              Image Detection
            </h3>

            <p>
              Upload an image and automatically detect whether
              faces are wearing masks.
            </p>

            <Link to="/detect">
              Try Detection →
            </Link>

          </div>


          <div className="feature-card">

            <div className="feature-icon">
              🎥
            </div>

            <h3>
              Live Detection
            </h3>

            <p>
              Use your webcam for real-time face mask detection
              with bounding boxes and confidence scores.
            </p>

            <Link to="/live">
              Open Camera →
            </Link>

          </div>


          <div className="feature-card">

            <div className="feature-icon">
              📊
            </div>

            <h3>
              Model Analytics
            </h3>

            <p>
              Explore the CNN model's accuracy, precision,
              recall, F1 score and confusion matrix.
            </p>

            <Link to="/analytics">
              View Analytics →
            </Link>

          </div>

        </div>

      </section>


      {/* How It Works */}
      <section className="home-section">

        <div className="section-heading">

          <p className="section-tag">
            SIMPLE WORKFLOW
          </p>

          <h2>
            How It Works
          </h2>

        </div>


        <div className="steps-grid">

          <div className="step-card">

            <span>01</span>

            <h3>
              Capture
            </h3>

            <p>
              Upload an image or start the webcam.
            </p>

          </div>


          <div className="step-card">

            <span>02</span>

            <h3>
              Detect
            </h3>

            <p>
              OpenCV identifies faces in the image.
            </p>

          </div>


          <div className="step-card">

            <span>03</span>

            <h3>
              Classify
            </h3>

            <p>
              The CNN classifies each face as MASK or NO MASK.
            </p>

          </div>


          <div className="step-card">

            <span>04</span>

            <h3>
              Result
            </h3>

            <p>
              The system displays the prediction and confidence.
            </p>

          </div>

        </div>

      </section>


      {/* CTA */}
      <section className="cta-section">

        <p className="section-tag">
          START DETECTING
        </p>

        <h2>
          See the AI model in action.
        </h2>

        <p>
          Upload an image or use your webcam to test the
          face mask detection system.
        </p>

        <Link to="/detect" className="primary-button">
          Start Detection →
        </Link>

      </section>

    </div>
  );
}


function Navbar() {
  return (
    <nav className="navbar">

      <Link to="/" className="logo">
        <span className="logo-icon">🛡️</span>
        Face<span>Guard</span>
      </Link>


      <div className="nav-links">

        <NavLink to="/" end>
          Home
        </NavLink>

        <NavLink to="/detect">
          Detect
        </NavLink>

        <NavLink to="/live">
          Live Camera
        </NavLink>

        <NavLink to="/analytics">
          Analytics
        </NavLink>

        <NavLink to="/about">
          About
        </NavLink>

      </div>

    </nav>
  );
}


function Footer() {
  return (
    <footer className="footer">

      <div>
        <h3>
          🛡️ Face<span>Guard</span>
        </h3>

        <p>
          Real-time AI-powered face mask detection.
        </p>
      </div>

      <div className="footer-links">

        <Link to="/detect">
          Detection
        </Link>

        <Link to="/live">
          Live Camera
        </Link>

        <Link to="/analytics">
          Analytics
        </Link>

        <Link to="/about">
          About
        </Link>

      </div>

      <p className="copyright">
        © 2026 FaceGuard. AI Face Mask Detection System.
      </p>

    </footer>
  );
}


function App() {
  return (
    <BrowserRouter>

      <Navbar />

      <main>
        <Routes>

          <Route
            path="/"
            element={<Home />}
          />

          <Route
            path="/detect"
            element={<Detect />}
          />

          <Route
            path="/live"
            element={<Live />}
          />

          <Route
            path="/analytics"
            element={<Analytics />}
          />

          <Route
            path="/about"
            element={<About />}
          />

        </Routes>
      </main>

      <Footer />

    </BrowserRouter>
  );
}


export default App;
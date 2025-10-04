Advanced Real-Time Cheating Detection System
Project Goal

To develop a robust, multi-modal, open-source system capable of detecting potential cheating behavior during online assessments by analyzing screen activity, webcam feed, and user behavioral biometrics in real-time.
Technical Stack (MVP)

    Core Logic: Python 3.10+

    Computer Vision: YOLOv8 (PyTorch)

    Real-Time Capture: OpenCV (cv2), mss, pynput

    ML/Anomaly Detection: scikit-learn

    User Interface (Proctor Dashboard): Streamlit

Architecture

The system employs a multi-threaded architecture to ensure real-time performance, running separate threads for data ingestion (Screen/Webcam/Behavioral) and inference (CV/Anomaly Detection). A unified scoring function aggregates results into a single "Cheating Confidence Score."
Phase 1: Foundation and Baseline Setup (Active)
1. Setup & Environment

    Clone this repository.

    Create and activate a Python virtual environment (venv).

    Install core dependencies listed in requirements.txt. (Note: requirements.txt will be created in an upcoming task).

2. Data Acquisition

    Run the initial capture scripts to verify system access to the webcam, screen, and keystroke events.

    Begin collecting initial, labeled datasets for custom object detection training.

3. Baseline Model

    Train the YOLOv8 model on a foundational dataset (e.g., detecting phones, secondary monitors, and note-taking activity).

Contribution

We use the Feature Branching workflow.

    Create a branch for your feature (git checkout -b feature/your-feature-name).

    Commit your changes (git commit -m 'feat: Added function X to module Y').

    Push to the branch (git push origin feature/your-feature-name).

    Open a Pull Request (PR) for review.

Current Leads

    Project Architect & Lead Developer: Gemini (Project Planning, ML Architecture)

    [Team Member 1]: [Assigned Tasks]

    [Team Member 2]: [Assigned Tasks]
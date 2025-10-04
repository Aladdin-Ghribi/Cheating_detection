import os

# --- PATH CONFIGURATION (Task P1.3) ---
# Base directory for the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data storage paths
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_CV_PATH = os.path.join(DATA_DIR, 'raw_cv')
RAW_BEHAVIORAL_PATH = os.path.join(DATA_DIR, 'raw_behavioral')
MODELS_PATH = os.path.join(BASE_DIR, 'models')

# Create directories if they don't exist
for path in [RAW_CV_PATH, RAW_BEHAVIORAL_PATH, MODELS_PATH]:
    os.makedirs(path, exist_ok=True)

# --- MODEL CONFIGURATION ---
YOLO_MODEL_NAME = "yolov8n.pt"  # Nano version for fast real-time inference
YOLO_MODEL_PATH = os.path.join(MODELS_PATH, YOLO_MODEL_NAME)
# Minimum confidence score for a detection to be considered valid
CONFIDENCE_THRESHOLD = 0.55

# --- REAL-TIME STREAM CONFIGURATION ---
WEBCAM_INDEX = 0        # Index of the default webcam
TARGET_FPS = 15         # Target processing FPS for the detection loop
# 0 or 1. Use 1 for the second monitor if available, or check your primary monitor index.
SCREEN_MONITOR_INDEX = 1
# (left, top, width, height) - specify area to capture
SCREEN_RESOLUTION = (100, 50, 1920, 1080)

# --- LOGGING AND BEHAVIORAL CONFIGURATION ---
LOG_FILE = os.path.join(BASE_DIR, 'session.log')
LOG_LEVEL = 'INFO'

# Keystroke Logger File Naming
BEHAVIORAL_LOG_FILE = os.path.join(RAW_BEHAVIORAL_PATH, 'behavioral_log.csv')

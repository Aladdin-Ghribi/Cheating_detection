import cv2
import time
import os
import threading
from ultralytics import YOLO
from detection_modules.capture import capture_webcam_frame, capture_screen_frame
from detection_modules.behavioral_logger import BehavioralLogger
from config import WEBCAM_INDEX, SCREEN_RESOLUTION, YOLO_MODEL_PATH, TARGET_FPS

# --- Phase 1: Main Application Setup ---
# This script focuses on verifying data capture and model loading.


def main():
    """Initializes and runs the primary data capture and logging modules."""
    print("--- Advanced Real-Time Cheating Detection System ---")
    print("Phase 1: Initializing Foundation Modules...")

    # 1. Start Behavioral Logger in a separate thread (Task P1.6)
    logger = BehavioralLogger()
    logger.start()
    print(f"Behavioral logger started. Logging to {logger.log_path}")

    # 2. Load the YOLO model (Task P1.8)
    # The model will download if not present in the specified path.
    try:
        model = YOLO(YOLO_MODEL_PATH)
        print(f"YOLOv8 model loaded successfully: {YOLO_MODEL_PATH}")
    except Exception as e:
        print(f"Error loading YOLO model: {e}")
        return

    # 3. Start the main CV inference loop (Webcam and Screen Capture Test)
    frame_delay = 1 / TARGET_FPS
    print(
        f"Starting real-time CV loop at approx. {TARGET_FPS} FPS (Ctrl+C to stop)...")

    try:
        while True:
            start_time = time.time()

            # --- Capture Data (Tasks P1.4 & P1.5) ---
            webcam_frame = capture_webcam_frame(WEBCAM_INDEX)
            screen_frame = capture_screen_frame(SCREEN_RESOLUTION)

            # Check if frames were captured successfully
            if webcam_frame is not None and screen_frame is not None:
                # Placeholder for detection (Actual detection logic will be in cv_pipeline.py in Phase 2)
                # For now, we just display the raw frames to verify capture

                # Resize screen frame to fit next to webcam for simultaneous display check
                webcam_h, webcam_w, _ = webcam_frame.shape
                screen_frame_resized = cv2.resize(
                    screen_frame, (webcam_w, webcam_h))

                # Concatenate frames side-by-side for verification
                combined_frame = cv2.hconcat(
                    [webcam_frame, screen_frame_resized])

                cv2.putText(combined_frame, f"Logging Events | FPS: {1.0 / (time.time() - start_time):.1f}", (
                    10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.imshow('Raw Input Streams (Webcam | Screen)',
                           combined_frame)

            # Handle exit and sleep for frame rate control
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Enforce target FPS
            elapsed_time = time.time() - start_time
            sleep_time = frame_delay - elapsed_time
            if sleep_time > 0:
                time.sleep(sleep_time)

    except KeyboardInterrupt:
        print("\nExiting application...")
    finally:
        # Cleanup
        logger.stop()
        cv2.destroyAllWindows()
        print("Application cleanup complete.")


if __name__ == "__main__":
    # Ensure the detection_modules directory structure exists
    os.makedirs('detection_modules', exist_ok=True)

    # Run the main function
    main()

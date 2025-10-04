import cv2
import mss
import numpy as np

# --- Task P1.4: Screen Capture Function ---


def capture_screen_frame(monitor_area: tuple) -> np.ndarray | None:
    """
    Captures a frame from the specified monitor area using mss.
    
    Args:
        monitor_area: A tuple defining the capture region (left, top, width, height).
    
    Returns:
        A NumPy array representing the captured screen frame (BGR format), or None on error.
    """
    try:
        sct = mss.mss()
        # mss expects a dict for monitor definition
        monitor = {
            "top": monitor_area[1],
            "left": monitor_area[0],
            "width": monitor_area[2],
            "height": monitor_area[3]
        }

        # Grab the screen image data
        sct_img = sct.grab(monitor)

        # Convert to numpy array (BGRA format)
        frame = np.array(sct_img)

        # Convert BGRA to BGR (OpenCV standard)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        return frame

    except Exception as e:
        # print(f"Screen capture error: {e}")
        return None

# --- Task P1.5: Webcam Capture Function ---


# Store the capture object globally to avoid reinitialization in the loop
_webcam_capture = None


def capture_webcam_frame(index: int) -> np.ndarray | None:
    """
    Captures a frame from the webcam using OpenCV.
    
    Args:
        index: The index of the webcam device (e.g., 0).
        
    Returns:
        A NumPy array representing the captured webcam frame (BGR format), or None on error.
    """
    global _webcam_capture

    # Initialize the capture object once
    if _webcam_capture is None:
        _webcam_capture = cv2.VideoCapture(index)
        # Attempt to set resolution for performance
        _webcam_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        _webcam_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if _webcam_capture.isOpened():
        ret, frame = _webcam_capture.read()
        if ret:
            return frame

    # Handle failure (e.g., camera unplugged, initialization failed)
    # print("Webcam not available or could not read frame.")
    return None


def release_webcam():
    """Releases the webcam capture object."""
    global _webcam_capture
    if _webcam_capture:
        _webcam_capture.release()
        _webcam_capture = None

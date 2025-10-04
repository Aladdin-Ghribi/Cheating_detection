import threading
import time
import csv
from datetime import datetime
from pynput import keyboard, mouse
from config import BEHAVIORAL_LOG_FILE


class BehavioralLogger(threading.Thread):
    """
    Task P1.6: Captures low-level keyboard and mouse events 
    in a separate, non-blocking thread and logs them to a CSV file.
    """

    def __init__(self):
        super().__init__()
        self.daemon = True  # Allows the program to exit even if threads are running
        self.running = False
        self.log_path = BEHAVIORAL_LOG_FILE
        self.log_file = None
        self.csv_writer = None

        # Setup listeners (initialized when thread starts)
        self.keyboard_listener = None
        self.mouse_listener = None

    def _init_log_file(self):
        """Initializes the CSV file and writes the header."""
        try:
            # Use 'a' (append) mode to continue logging or 'w' (write) to start new
            self.log_file = open(self.log_path, 'a', newline='')
            self.csv_writer = csv.writer(self.log_file)

            # Check if file is new/empty before writing header
            if self.log_file.tell() == 0:
                self.csv_writer.writerow(
                    ['timestamp', 'event_type', 'key_detail', 'mouse_x', 'mouse_y', 'mouse_button'])
        except Exception as e:
            print(f"Error initializing behavioral log file: {e}")
            self.stop()

    def _on_press(self, key):
        """Callback for key press events."""
        try:
            key_detail = str(key).replace("'", "")
            self._log_event('key_press', key_detail)
        except Exception:
            pass  # Ignore unprintable keys gracefully

    def _on_release(self, key):
        """Callback for key release events."""
        try:
            key_detail = str(key).replace("'", "")
            self._log_event('key_release', key_detail)
        except Exception:
            pass  # Ignore unprintable keys gracefully

    def _on_click(self, x, y, button, pressed):
        """Callback for mouse click events."""
        event_type = 'mouse_down' if pressed else 'mouse_up'
        self._log_event(event_type, 'click', x, y, str(button))

    def _on_move(self, x, y):
        """Callback for mouse move events (logged less frequently in run())."""
        # Mouse movement is too verbose for a direct callback log; logged via sampling in run()
        pass

    def _log_event(self, event_type, key_detail=None, x=None, y=None, button=None):
        """Writes an event record to the CSV file."""
        if self.csv_writer:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            self.csv_writer.writerow(
                [timestamp, event_type, key_detail, x, y, button])
            self.log_file.flush()  # Force write to disk immediately

    def run(self):
        """The main thread execution loop."""
        self.running = True
        self._init_log_file()

        # Initialize listeners
        self.keyboard_listener = keyboard.Listener(
            on_press=self._on_press, on_release=self._on_release)
        self.mouse_listener = mouse.Listener(
            on_click=self._on_click, on_move=self._on_move)

        self.keyboard_listener.start()
        self.mouse_listener.start()

        # Keep the thread alive, logging mouse movement coarsely
        while self.running:
            # Note: Mouse position is logged in the click handler.
            # Continuous movement logging is disabled due to massive file size, unless enabled here.
            # Example (disabled by default): self._log_event('mouse_move', x=mouse.Controller().position[0], y=mouse.Controller().position[1])
            time.sleep(1)  # Sleep to keep the thread alive

        # Stop listeners gracefully
        if self.keyboard_listener and self.keyboard_listener.is_alive():
            self.keyboard_listener.stop()
        if self.mouse_listener and self.mouse_listener.is_alive():
            self.mouse_listener.stop()

        if self.log_file:
            self.log_file.close()

    def stop(self):
        """Signals the thread to stop execution."""
        self.running = False
        print("Behavioral logger signaled to stop.")

# End of BehavioralLogger class

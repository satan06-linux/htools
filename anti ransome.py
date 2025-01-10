import os
import time
import hashlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Directory to monitor
DIRECTORY_TO_MONITOR = "/path/to/your/directory"

known_hashes = {
    "file1.txt": "hash1",
    "file2.txt": "hash2",
    # Add more files and their hashes here
}

class AntiRansomwareHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        file_name = os.path.basename(file_path)
        
        # Calculate the hash of the modified file
        file_hash = self.calculate_file_hash(file_path)
        
        # Check if the file's hash has changed
        if file_name in known_hashes and known_hashes[file_name] != file_hash:
            print(f"WARNING: File {file_name} has been modified and may be encrypted by ransomware!")
            # Take action here, such as quarantining the file or alerting the user

    @staticmethod
    def calculate_file_hash(file_path):
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()

if __name__ == "__main__":
    event_handler = AntiRansomwareHandler()
    observer = Observer()
    observer.schedule(event_handler, path=DIRECTORY_TO_MONITOR, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

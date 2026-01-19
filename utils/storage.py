import json
import os
from utils.logger import log

class JsonDB:
    def __init__(self, folder_path="data"):
        self.folder_path = folder_path
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
    
    def _get_path(self, filename):
        if not filename.endswith(".json"):
            filename += ".json"
        return os.path.join(self.folder_path, filename)

    def load(self, filename, default=None):
        """
        Loads data from a JSON file.
        If file doesn't exist, returns default (or empty dict) and creates the file.
        """
        path = self._get_path(filename)
        if default is None:
            default = {}
            
        if not os.path.exists(path):
            self.save(filename, default)
            return default
            
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            log.error(f"Failed to load {filename}: {e}")
            return default

    def save(self, filename, data):
        """
        Saves data to a JSON file (Atomic-ish write).
        """
        path = self._get_path(filename)
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            log.error(f"Failed to save {filename}: {e}")

    def update(self, filename, key, value):
        """
        Updates a specific key in the JSON file.
        """
        data = self.load(filename)
        data[key] = value
        self.save(filename, data)

# Global Instance
db = JsonDB(folder_path="data")

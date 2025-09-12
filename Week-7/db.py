# db.py
import sqlite3
import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._connection = None
        return cls._instance

    def get_connection(self):
        if self._connection is None:
            self._connection = sqlite3.connect('app.db', check_same_thread=False)
        return self._connection
    
    def close_connection(self):
        if self._connection:
            self._connection.close()
            self._connection = None

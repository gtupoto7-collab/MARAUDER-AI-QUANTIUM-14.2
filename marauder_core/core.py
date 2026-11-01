import sqlite3
import os

class MarauderCore:
    def __init__(self, target_url):
        self.target_url = target_url
        # Tor прокси конфигурация
        self.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        self.db_path = "news_database.db"
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tool_master_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                module TEXT,
                status INTEGER,
                message TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    def log(self, module, status, message):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tool_master_logs (module, status, message) VALUES (?, ?, ?)", (module, status, message))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"[!] SQLite Log Error: {e}")

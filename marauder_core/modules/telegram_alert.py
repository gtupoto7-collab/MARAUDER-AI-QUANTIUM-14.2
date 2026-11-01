import requests
import sqlite3

class TelegramReporter:
    def __init__(self, core_instance, token="YOUR_BOT_TOKEN", chat_id="YOUR_CHAT_ID"):
        self.core = core_instance
        self.token = token
        self.chat_id = chat_id

    def send_alert(self, message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": f"🚨 [MARAUDER-AL ALERT]\n{message}"}
        try:
            res = requests.post(url, json=payload, proxies=self.core.proxies, timeout=10)
            if res.status_code == 200:
                print("    [+] Известието е изпратено успешно в Telegram!")
        except Exception as e:
            print(f"    [!] Грешка при изпращане до Telegram: {e}")

    def run_report_to_telegram(self):
        print(f"\n--- [ MARAUDER-AL TELEGRAM REPORTER ] ---")
        try:
            conn = sqlite3.connect(self.core.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT module, status, message FROM tool_master_logs ORDER BY id DESC LIMIT 5")
            rows = cursor.fetchall()
            conn.close()
            
            summary = "Последни одит логове от лабораторията:\n"
            for row in rows:
                summary += f"[{row[0]}] Status {row[1]}: {row[2][:50]}\n"
            
            self.send_alert(summary)
            self.core.log("TELEGRAM_REPORTER", 200, "Alert sent to Telegram.")
        except Exception as e:
            print(f"[!] Грешка при четене от базата за Telegram: {e}")

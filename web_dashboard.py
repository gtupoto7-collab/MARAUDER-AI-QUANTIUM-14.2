from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)
DB_PATH = "news_database.db"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>MARAUDER-AL Lab Dashboard</title>
    <style>
        body { background-color: #0d1117; color: #58a6ff; font-family: monospace; padding: 20px; }
        h1 { color: #f85149; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #30363d; padding: 10px; text-align: left; }
        th { background-color: #161b22; color: #c9d1d9; }
        tr:nth-child(even) { background-color: #11161d; }
    </style>
</head>
<body>
    <h1>[!] MARAUDER-AL FRAMEWORK - LIVE DASHBOARD</h1>
    <p>Централна SQLite база данни: одит логове в реално време</p>
    <table>
        <tr><th>ID</th><th>Модул</th><th>Статус</th><th>Съобщение</th><th>Време</th></tr>
        {% for row in logs %}
        <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
            <td>{{ row[3] }}</td>
            <td>{{ row[4] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route('/')
def index():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, module, status, message, timestamp FROM tool_master_logs ORDER BY id DESC LIMIT 50")
    logs = cursor.fetchall()
    conn.close()
    return render_template_string(HTML_TEMPLATE, logs=logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

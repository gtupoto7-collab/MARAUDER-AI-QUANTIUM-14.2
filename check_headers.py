import requests
import sqlite3

# Конфигурация на Tor SOCKS5 прокси
proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

target_url = "https://zapernik.com"

# Инициализиране на SQLite базата данни
db_name = "news_database.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Създаване на таблица за потребителите, ако не съществува
cursor.execute('''
    CREATE TABLE IF NOT EXISTS audited_users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        name TEXT
    )
''')
conn.commit()

print(f"[->] Стартиране на пълен одит и запис в базата за {target_url} през Tor...\n")

try:
    # 1. Проверка на основните хедъри за сигурност
    response = requests.get(target_url, proxies=proxies, timeout=15)
    print(f"[+] HTTP Статус код на началната страница: {response.status_code}")
    
    security_headers = [
        'Strict-Transport-Security',
        'Content-Security-Policy',
        'X-Frame-Options',
        'X-Content-Type-Options',
        'Referrer-Policy'
    ]
    
    print("\n--- Анализ на хедърите за сигурност ---")
    for header in security_headers:
        if header in response.headers:
            print(f"[V] {header}: Наличен")
        else:
            print(f"[!] Липсва: {header}")

    # 2. Проверка за уязвими/достъпни стандартни файлове
    sensitive_paths = [
        "/xmlrpc.php",
        "/readme.html",
        "/license.txt"
    ]
    
    print("\n--- Проверка за чувствителни WordPress endpoint-и ---")
    for path in sensitive_paths:
        full_url = target_url + path
        res = requests.get(full_url, proxies=proxies, timeout=10)
        if res.status_code == 200:
            print(f"[!] ВНИМАНИЕ (200 OK): {path} е публично достъпен!")
        elif res.status_code == 403:
            print(f"[V] Защитен (403 Forbidden): {path}")
        else:
            print(f"[-] Статус {res.status_code}: {path}")

    # 3. Автоматично извличане на потребители и запис в SQLite
    users_url = target_url + "/wp-json/wp/v2/users"
    print(f"\n--- Сканиране на WP REST API и запис в базата ---")
    users_res = requests.get(users_url, proxies=proxies, timeout=10)
    
    if users_res.status_code == 200:
        users_data = users_res.json()
        print(f"[+] Успешно извлечени {len(users_data)} потребителски профила:")
        
        for user in users_data:
            user_id = user.get('id')
            username = user.get('slug')
            name = user.get('name')
            
            # Запис в базата данни (с обновяване при промяна)
            cursor.execute('''
                INSERT OR REPLACE INTO audited_users (id, username, name)
                VALUES (?, ?, ?)
            ''', (user_id, username, name))
            
            print(f"    [v] Записан в SQLite -> ID: {user_id} | Потребител: {username} | Име: {name}")
            
        conn.commit()
        print(f"[+] Всички потребители са успешно съхранени в '{db_name}'!")
    else:
        print(f"[-] REST API users endpoint не върна данни (Статус: {users_res.status_code})")

except Exception as e:
    print(f"[!] Грешка при връзката през Tor: {e}")

finally:
    # Затваряне на връзката с базата
    conn.close()

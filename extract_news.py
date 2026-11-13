import requests
from bs4 import BeautifulSoup

# Конфигурация на Tor SOCKS5 прокси
proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

# Четене на линковете от файла
try:
    with open('latest_news.txt', 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("[-] Файлът latest_news.txt не е намерен!")
    exit()

print(f"[+] Заредени {len(urls)} линка за обработка през Tor...")

for url in urls:
    print(f"\n[->] Извличане на: {url}")
    try:
        # Извършване на анонимна заявка през Tor
        response = requests.get(url, proxies=proxies, timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Извличане на заглавието
            title = soup.find('h1')
            title_text = title.get_text(strip=True) if title else "Няма заглавие"
            
            # Извличане на основния текст на статията (според WordPress структурата)
            content_div = soup.find('div', class_='entry-content') or soup.find('article')
            if content_div:
                # Премахване на излишни скриптове/реклами ако има
                for script in content_div(["script", "style"]):
                    script.decompose()
                article_text = content_div.get_text(separator='\n', strip=True)
            else:
                article_text = "Не е открито съдържание в стандартен контейнер."
                
            print(f"[+] Заглавие: {title_text}")
            print(f"[+] Обем на текста: {len(article_text)} символа")
            
            # Можеш да запишеш резултата във файл или да го обработваш
        else:
            print(f"[-] Сървърът върна код: {response.status_code}")
    except Exception as e:
        print(f"[!] Грешка при връзката: {e}")
import sqlite3
import requests
from bs4 import BeautifulSoup

# Конфигурация на Tor SOCKS5 прокси
proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

# Инициализиране на SQLite база данни
db_name = 'news_database.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Създаване на таблица за статиите (ако не съществува)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT UNIQUE,
        title TEXT,
        content TEXT
    )
''')
conn.commit()

# Четене на линковете от файла
try:
    with open('latest_news.txt', 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("[-] Файлът latest_news.txt не е намерен!")
    conn.close()
    exit()

print(f"[+] Заредени {len(urls)} линка за обработка през Tor...")

for url in urls:
    print(f"\n[->] Обработка: {url}")
    try:
        response = requests.get(url, proxies=proxies, timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Извличане на заглавието
            title = soup.find('h1')
            title_text = title.get_text(strip=True) if title else "Няма заглавие"
            
            # Извличане на съдържанието
            content_div = soup.find('div', class_='entry-content') or soup.find('article')
            if content_div:
                for script in content_div(["script", "style"]):
                    script.decompose()
                article_text = content_div.get_text(separator='\n', strip=True)
            else:
                article_text = "Не е открито съдържание в стандартен контейнер."
                
            # Записване в SQLite базата данни (с игнориране при дублиране на URL)
            cursor.execute('''
                INSERT OR IGNORE INTO articles (url, title, content)
                VALUES (?, ?, ?)
            ''', (url, title_text, article_text))
            conn.commit()
            
            print(f"[+] Записано в базата: {title_text[:40]}...")
        else:
            print(f"[-] Сървърът върна код: {response.status_code}")
    except Exception as e:
        print(f"[!] Грешка при връзката: {e}")

# Затваряне на връзката с базата
conn.close()
print(f"\n[+] Всички данни са успешно съхранени в '{db_name}'!")

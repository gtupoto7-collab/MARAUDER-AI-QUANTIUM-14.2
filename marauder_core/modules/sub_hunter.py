import requests
from urllib.parse import urlparse

class SubHunter:
    def __init__(self, core_instance):
        self.core = core_instance

    def run_sub_hunter(self):
        print(f"\n--- [ MARAUDER-AL SUBDOMAIN & DIRECTORY HUNTER ] ---")
        parsed = urlparse(self.core.target_url)
        base_domain = parsed.netloc
        scheme = parsed.scheme
        
        wordlist = ["admin", "api", "test", "dev", "login", "portal", "secure", "dashboard", "db", "shop"]
        print(f"[->] Сканиране на поддомейни и директории за {base_domain} през Tor...")

        for word in wordlist:
            sub_url = f"{scheme}://{word}.{base_domain}"
            dir_url = f"{self.core.target_url.rstrip('/')}/{word}"
            
            for test_url in [sub_url, dir_url]:
                try:
                    res = requests.get(test_url, proxies=self.core.proxies, timeout=8)
                    status = res.status_code
                    if status in [200, 301, 302, 403]:
                        print(f"    [+] Жив обект открит: {test_url} (Статус: {status})")
                        self.core.log("SUB_HUNTER", status, f"Found live target: {test_url}")
                except Exception:
                    pass
                    
        print("[+] Sub_hunter модулът завърши работа.")
        self.core.log("SUB_HUNTER", 200, "Subdomain scan completed.")

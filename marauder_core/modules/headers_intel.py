import requests

class HeaderAnalyzer:
    def __init__(self, core_instance):
        self.core = core_instance

    def run_header_analysis(self):
        print(f"\n--- [ MARAUDER-AL OSINT & HEADER ANALYZER ] ---")
        print(f"[->] Анализ на HTTP хедъри за {self.core.target_url} през Tor...")

        try:
            res = requests.get(self.core.target_url, proxies=self.core.proxies, timeout=10)
            headers = res.headers
            
            print(f"\n[+] Открити HTTP хедъри:")
            for k, v in headers.items():
                print(f"    {k}: {v}")
                
            security_headers = ['Content-Security-Policy', 'Strict-Transport-Security', 'X-Frame-Options', 'X-XSS-Protection', 'X-Content-Type-Options']
            missing = []
            
            for sh in security_headers:
                if sh not in headers:
                    missing.append(sh)
                    
            if missing:
                print(f"\n    [!] Липсващи важни сигурностни хедъри: {', '.join(missing)}")
                self.core.log("HEADERS_INTEL", 200, f"Missing security headers: {', '.join(missing)}")
            else:
                print(f"\n    [+] Всички главни сигурностни хедъри са налични.")
                self.core.log("HEADERS_INTEL", 200, "All major security headers present.")
                
        except Exception as e:
            print(f"[!] Грешка при анализ на хедърите през Tor: {e}")
            self.core.log("HEADERS_INTEL", 500, f"Error analyzing headers: {e}")

import requests
import json
import time
from marauder_core.modules.scanner import TargetScanner
from marauder_core.modules.stress import StressTester
from marauder_core.modules.vuln import VulnerabilityChecker
from marauder_core.modules.brute import BruteForcer

class OllamaMasterAgent:
    def __init__(self, core_instance):
        self.core = core_instance
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model_name = "phi3:mini"

    def ask_ollama(self, prompt):
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }
        try:
            res = requests.post(self.ollama_url, json=payload, timeout=30)
            if res.status_code == 200:
                return res.json().get("response", "")
        except Exception as e:
            print(f"[!] Грешка при връзка с локалния Ollama сървър: {e}")
        return "Няма отговор от Ollama."

    def run_extra_checks(self):
        print("\n[+] 5. Стартиране на допълнителни скрити проверки (Sensitive Files)...")
        sensitive_paths = ["/robots.txt", "/.git/HEAD", "/xmlrpc.php", "/wp-admin/"]
        
        for path in sensitive_paths:
            full_url = f"{self.core.target_url}{path}"
            try:
                response = requests.get(full_url, proxies=self.core.proxies, timeout=10)
                status = response.status_code
                print(f"    [->] Проверка на {path} -> Статус: {status}")
                
                if status == 200:
                    print(f"        [!] НАМЕРЕН ДОСТЪПЕН ОБЕКТ: {path}")
                    self.core.log("EXTRA_CHECK", 200, f"Sensitive path found: {path}")
            except Exception as e:
                print(f"    [!] Грешка при достъп до {path} през Tor")

    def run_master_orchestration(self):
        print(f"\n--- [ MARAUDER-AL OLLAMA MASTER AGENT ] ---")
        print(f"[->] Свързване с локалния Ollama модел ({self.model_name})...")
        
        ai_prompt = f"Target: {self.core.target_url}. Анализирай какви стъпки да предприемем за кибер одит (Recon, Stress, Vuln, Brute) в кратък текст."
        advice = self.ask_ollama(ai_prompt)
        print(f"\n[+] Ollama Agent Strategy:\n{advice}\n")
        
        self.core.log("OLLAMA_AGENT", 200, f"Strategy generated: {advice[:100]}...")

        print("[+] 1. Стартиране на Recon модул...")
        scanner = TargetScanner(self.core)
        scanner.run_recon()

        print("\n[+] 2. Стартиране на Vulnerability Check модул...")
        vuln = VulnerabilityChecker(self.core)
        vuln.run_check()

        print("\n[+] 3. Стартиране на Stress Test модул...")
        stress = StressTester(self.core, total_requests=10, max_threads=3)
        stress.run_stress_test()

        print("\n[+] 4. Стартиране на Brute-Force модул...")
        brute = BruteForcer(self.core)
        brute.run_brute()

        print("\n[+] Всички инструменти минаха успешно. Резултатите са записани в SQLite!")
        self.core.log("OLLAMA_AGENT", 200, "Full automated agent workflow completed successfully.")

        self.run_extra_checks()

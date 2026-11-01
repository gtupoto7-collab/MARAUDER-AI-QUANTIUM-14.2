import requests
import json

class MultiAgentSwarm:
    def __init__(self, core_instance):
        self.core = core_instance
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model_name = "phi3:mini"

    def ask_role(self, role_prompt, target):
        payload = {
            "model": self.model_name,
            "prompt": f"{role_prompt} Target: {target}",
            "stream": False
        }
        try:
            res = requests.post(self.ollama_url, json=payload, timeout=30)
            if res.status_code == 200:
                return res.json().get("response", "")
        except Exception as e:
            return f"Error: {e}"
        return "No response."

    def run_swarm(self):
        print(f"\n--- [ MARAUDER-AL MULTI-AGENT SWARM ] ---")
        target = self.core.target_url
        
        print("[->] Роля 1: Recon Specialist анализира целта...")
        recon_advice = self.ask_role("You are an expert Reconnaissance specialist. Give 2 key reconnaissance tips for:", target)
        print(f"    [AI Recon]: {recon_advice[:150]}...\n")

        print("[->] Роля 2: Vulnerability Analyst търси пробиви...")
        vuln_advice = self.ask_role("You are a senior Vuln Analyst. What are top 2 web vulnerabilities to check for on:", target)
        print(f"    [AI Vuln]: {vuln_advice[:150]}...\n")

        self.core.log("MULTI_AGENT", 200, "Multi-agent swarm completed analysis.")

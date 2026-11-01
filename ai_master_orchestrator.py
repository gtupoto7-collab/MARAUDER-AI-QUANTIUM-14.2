import sys
import argparse
import random
import time
import json
import requests
import concurrent.futures
from curl_cffi import requests as crequests
from marauder_core.core import MarauderCore

def launch_tls_agent(agent_id, target, proxy):
    browser_profiles = ["chrome110", "chrome120", "firefox110", "safari15_3"]
    chosen_browser = random.choice(browser_profiles)
    
    start_t = time.time()
    try:
        response = crequests.get(
            target, 
            impersonate=chosen_browser, 
            proxy=proxy, 
            timeout=10
        )
        duration = time.time() - start_t
        return agent_id, response.status_code, chosen_browser, duration, None
    except Exception as e:
        duration = time.time() - start_t
        return agent_id, 0, chosen_browser, duration, str(e)

def ask_local_ai(target, success_count, total_agents, avg_duration):
    ollama_url = "http://localhost:11434/api/generate"
    prompt = (
        f"Target: {target}\n"
        f"Total Swarm Agents: {total_agents}\n"
        f"Successful Tor/TLS Hits: {success_count}\n"
        f"Average Response Duration: {avg_duration:.2f}s\n"
        "Act as an elite autonomous Red Team Commander. "
        "Analyze these swarm metrics and give a precise 3-step tactical recommendation "
        "on how to bypass remaining defenses and optimize the next wave."
    )
    
    payload = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    print(f"\n[+] Изпращане на данните от рояка към локалния AI мозък (llama3.2)...")
    try:
        res = requests.post(ollama_url, json=payload, timeout=120)
        if res.status_code == 200:
            return res.json().get("response", "No response from AI.")
        else:
            return "[!] Ollama сървърът върна грешка."
    except Exception as e:
        return f"[!] Неуспешна връзка с локалния AI: {e}"

def main():
    parser = argparse.ArgumentParser(description="MARAUDER-AL AI-Driven Master Orchestrator")
    parser.add_argument("-t", "--target", required=True, help="Целеви URL адрес")
    parser.add_argument("-c", "--count", type=int, default=30, help="Брой агенти в рояка")
    args = parser.parse_args()

    print(f"\n==========================================")
    print(f"   MARAUDER-AL AI-DRIVEN SWARM v4.0")
    print(f"   Target: {args.target} | Agents: {args.count}")
    print(f"==========================================")

    core = MarauderCore(target_url=args.target)
    proxy = "socks5://127.0.0.1:9050"
    
    start_time = time.time()
    success_count = 0
    total_duration = 0.0

    # Стартираме рояка паралелно
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(launch_tls_agent, i, args.target, proxy) for i in range(1, args.count + 1)]
        
        for future in concurrent.futures.as_completed(futures):
            agent_id, status, browser, duration, error = future.result()
            total_duration += duration
            if status > 0:
                success_count += 1
                print(f"    [+] [AI Агент #{agent_id}] Профил: {browser} | Статус: {status} | Време: {duration:.2f}s")
                core.log(f"AI_AGENT_{agent_id}", status, f"Impersonated {browser} via Tor in {duration:.2f}s")
            else:
                print(f"    [!] [AI Агент #{agent_id}] Мрежов timeout/грешка през Tor.")

    elapsed = time.time() - start_time
    avg_duration = (total_duration / args.count) if args.count > 0 else 0

    print(f"\n[+] Мрежовият удар приключи за {elapsed:.2f} секунди.")
    
    # Подаваме резултатите на AI мозъка за анализ
    ai_analysis = ask_local_ai(args.target, success_count, args.count, avg_duration)
    
    print(f"\n==========================================")
    print(f"   AI RED TEAM COMMANDER TACTICAL REPORT:")
    print(f"==========================================")
    print(ai_analysis)
    print(f"==========================================")
    
    core.log("AI_TACTICAL_REPORT", 200, "AI Red Team analysis generated successfully.")

if __name__ == "__main__":
    main()

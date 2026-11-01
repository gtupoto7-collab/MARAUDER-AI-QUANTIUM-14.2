import sys
import argparse
import random
import time
import concurrent.futures
from curl_cffi import requests as crequests
from marauder_core.core import MarauderCore

def launch_tls_agent(agent_id, target, proxy):
    browser_profiles = ["chrome110", "chrome120", "firefox110", "safari15_3"]
    chosen_browser = random.choice(browser_profiles)
    
    try:
        # Изпращаме заявка с маскиран TLS отпечатък и Tor прокси
        response = crequests.get(
            target, 
            impersonate=chosen_browser, 
            proxy=proxy, 
            timeout=10
        )
        return agent_id, response.status_code, chosen_browser, None
    except Exception as e:
        return agent_id, 0, chosen_browser, str(e)

def main():
    parser = argparse.ArgumentParser(description="MARAUDER-AL Master TLS & Swarm Orchestrator")
    parser.add_argument("-t", "--target", required=True, help="Целеви URL адрес")
    parser.add_argument("-c", "--count", type=int, default=100, help="Брой агенти в рояка")
    args = parser.parse_args()

    print(f"\n==========================================")
    print(f"   MARAUDER-AL OMNI-MASTER SWARM v3.0")
    print(f"   Target: {args.target} | Agents: {args.count}")
    print(f"==========================================")

    core = MarauderCore(target_url=args.target)
    proxy = "socks5://127.0.0.1:9050"
    
    start_time = time.time()
    success_count = 0

    # Използваме ThreadPoolExecutor за паралелно изпълнение с TLS рандомизация през Tor
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(launch_tls_agent, i, args.target, proxy) for i in range(1, args.count + 1)]
        
        for future in concurrent.futures.as_completed(futures):
            agent_id, status, browser, error = future.result()
            if status > 0:
                success_count += 1
                print(f"    [+] [Омега Агент #{agent_id}] Профил: {browser} | Статус: {status}")
                core.log(f"OMNI_AGENT_{agent_id}", status, f"Impersonated {browser} via Tor")
            else:
                print(f"    [!] [Омега Агент #{agent_id}] Мрежова грешка през Tor.")

    elapsed = time.time() - start_time
    print(f"\n[+] Омнисветовният мастър рояк приключи работа!")
    print(f"    [->] Успешни удари: {success_count}/{args.count}")
    print(f"    [->] Време за изпълнение: {elapsed:.2f} секунди")
    core.log("OMNI_MASTER_COMPLETE", 200, f"Completed {args.count} TLS-randomized requests in {elapsed:.2f}s")

if __name__ == "__main__":
    main()

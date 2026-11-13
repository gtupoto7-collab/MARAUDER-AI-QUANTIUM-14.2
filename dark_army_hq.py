import sys
import argparse
import time
from marauder_core.core import MarauderCore

def mobilize_division(division_name, count, target):
    print(f"\n[+] [mobilizatsia] Divizia '{division_name}' mobilizira {count} agenta kam tsel: {target}")
    time.sleep(0.5)
    print(f"    [->] Vsyaka edna ot edinitsite v sluzhba '{division_name}' e na pozitsia!")

def main():
    parser = argparse.ArgumentParser(description="DARKWEBARMY Supreme Command HQ")
    parser.add_argument("-t", "--target", required=True, help="Tselevi URL adres")
    parser.add_argument("-c", "--count", type=int, default=100000, help="Agenti za vsyaka voenna sluzhba")
    args = parser.parse_args()

    print(f"\n==========================================")
    print(f"   DARKWEBARMY SUPREME COMMAND HQ (v5.0)")
    print(f"   Target: {args.target} | Force per Division: {args.count}")
    print(f"==========================================")

    core = MarauderCore(target_url=args.target)

    mobilize_division("OSINT Recon Division", args.count, args.target)
    mobilize_division("Heavy Artillery Division", args.count, args.target)
    mobilize_division("SEAL Cyber Division", args.count, args.target)

    print(f"\n[+] [AI Shtab] Analizira vsichki danni ot armiite chrez lokalnia mozak...")
    print(f"[+] Vsyaka sluzhba si znae zadachata. Nyama propusk na milimetar!")
    
    core.log("HQ_MOBILIZATION", 200, f"All divisions mobilized successfully against {args.target}")
    print(f"\n[+] DARKWEBARMY e v pulna bojna gotovnost!")

if __name__ == "__main__":
    main()

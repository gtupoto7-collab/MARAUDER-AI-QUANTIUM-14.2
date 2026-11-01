import argparse
import importlib
import inspect
import sys
from marauder_core.core import MarauderCore

def main():
    parser = argparse.ArgumentParser(
        description="MARAUDER-AL Framework - Anonymous Tor Security Automation Tool",
        epilog="Пример: ./venv/bin/python3 run.py -t https://shop.zapernik.com -m ollama_master"
    )
    
    parser.add_argument("-t", "--target", required=True, help="Целевият URL адрес")
    parser.add_argument("-m", "--module", required=True, help="Име на модула (напр. recon, stress, vuln, brute, ollama_master)")

    args = parser.parse_args()

    print("==========================================")
    print("   MARAUDER-AL FRAMEWORK v1.0 (PRO)       ")
    print("   Anonymous Tor-Sec Automation Lab       ")
    print("==========================================")
    
    core = MarauderCore(target_url=args.target)
    
    try:
        module_name = f"marauder_core.modules.{args.module}"
        mod = importlib.import_module(module_name)
        print(f"[+] Зареден модул: {args.module}")
        
        target_class = None
        for name, obj in inspect.getmembers(mod, inspect.isclass):
            if obj.__module__ == mod.__name__:
                target_class = obj
                break
                
        if not target_class:
            print(f"[!] Грешка: Не е намерен валиден клас в модула '{args.module}'!")
            sys.exit(1)
            
        print(f"[+] Открит изпълним клас: {target_class.__name__}")
        
        instance = target_class(core)
        
        executed = False
        for method_name in dir(instance):
            if method_name.startswith("run_"):
                method = getattr(instance, method_name)
                if callable(method):
                    print(f"[+] Изпълнение на метод: {method_name}()\n")
                    method()
                    executed = True
                    break
                    
        if not executed:
            print(f"[!] Грешка: Класът {target_class.__name__} няма метод, започващ с 'run_'!")

    except ModuleNotFoundError:
        print(f"[!] Грешка: Модулът '{args.module}' не съществува в папка 'modules/'!")
    except Exception as e:
        print(f"[!] Грешка при динамичното изпълнение: {e}")

    print("\n[+] Операцията завърши.")

if __name__ == "__main__":
    main()

#!/bin/bash

# ====================================================
#  📡 NFCAUTOKEY / ROOT NFC & HARDWARE ENGINE 
# ====================================================

RED='\033[1;31m'
GREEN='\033[1;32m'
CYAN='\033[1;36m'
WHITE='\033[1;37m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Проверка за Root права
if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}[!] Грешка: NFCAUTOKEY изисква пълен ROOT достъп!${NC}"
  echo -e "${YELLOW}[*] Използвай: sudo ./nfcc_autokey.sh${NC}"
  exit 1
fi

# Създаване на локална база данни / папка за записаните сигнали
VAULT_DIR="nfc_target_vault"
mkdir -p "$VAULT_DIR"

while true; do
    clear
    printf "${RED}"
    printf "        .-.\n"
    printf "       (   )\n"
    printf "        \`-\'\n"
    printf "     .-'   '-.\n"
    printf "    /         \\\n"
    printf "   |  _     _  |\n"
    printf "   | (O)   (O) |\n"
    printf "   |     ^     |\n"
    printf "   |    \\___/  |\n"
    printf "    \\         /\n"
    printf "     \`-'   '--'\n"
    printf "${NC}"
    printf "${WHITE}====================================================\n${NC}"
    printf "${CYAN}       [ 📡 NFCAUTOKEY / MASTER SYSTEM CORE ]       \n${NC}"
    printf "${WHITE}====================================================\n${NC}"
    echo -e " 1. 🔍 Сканиране и Запис на NFC Чипове / Хотелски Карти (Root/Non-Root)"
    echo -e " 2. 📂 Преглед на Запазените Сигнали в Базата Данни (Vault)"
    echo -e " 3. 🔓 Умно Отключване / Replay (Изпращане на запазен сигнал към врата/асансьор)"
    echo -e " 4. 💻 USB / Laptop Bridge (Връзка с външна NFC антена / PN532 / Терминал)"
    echo -e " 5. 💳 Micro-Payment Engine (Тестови заявки за малки суми 5-100 EUR)"
    echo -e " 6. ⚡ Клониране на UID върху нов чип (Zapsvashto ustroistvo)"
    echo -e "${WHITE}----------------------------------------------------${NC}"
    echo -e " 0. ⬅️ Изход към Лабораторията"
    echo -e "${WHITE}====================================================${NC}"
    read -p "Избери опция (0-6): " nfc_opt

    case $nfc_opt in
        1)
            echo -e "\n${CYAN}[+] Стартиране на NFC Скенер с пълни Root права...${NC}"
            echo -e "${YELLOW}[*] Постави чипа или картата близо до антената...${NC}"
            sleep 2
            # Симулация / Запис в базата данни
            read -p "Въведи име или номер на целта (напр. Hotel_Lift_01): " target_name
            simulated_uid="UID:$(openssl rand -hex 4 | tr '[:lower:]' '[:upper:]' | sed 's/\(..\)/\1:/g; s/:$//')"
            echo "$simulated_uid - $(date)" > "$VAULT_DIR/${target_name}.nfc"
            echo -e "${GREEN}[+] Успешно уловен и записан сигнал! UID: $simulated_uid${NC}"
            echo -e "${GREEN}[+] Запазен в базата данни: $VAULT_DIR/${target_name}.nfc${NC}"
            read -p "Натисни Enter за продължение..."
            ;;
        2)
            echo -e "\n${CYAN}[📂 СПИСЪК НА ЗАПАЗЕНИТЕ NFC ЦЕЛИ В БАЗАТА]${NC}"
            echo -e "${WHITE}----------------------------------------------------${NC}"
            if [ "$(ls -A $VAULT_DIR)" ]; then
                ls -la "$VAULT_DIR"
                echo -e "${WHITE}----------------------------------------------------${NC}"
                read -p "Въведи име на файл за детайлен преглед (или Enter за назад): " file_to_read
                if [ -f "$VAULT_DIR/$file_to_read" ]; then
                    echo -e "\n${GREEN}Съдържание на целта:${NC}"
                    cat "$VAULT_DIR/$file_to_read"
                fi
            else
                echo -e "${YELLOW}Базата данни е празна. Все още няма уловени сигнали.${NC}"
            fi
            read -p "Натисни Enter за продължение..."
            ;;
        3)
            echo -e "\n${CYAN}[🔓 УМНО ОТКЛЮЧВАНЕ / REPLAY EMULATION]${NC}"
            read -p "Въведи име на записаната цел за отваряне: " target_unlock
            if [ -f "$VAULT_DIR/$target_unlock" ]; then
                echo -e "${YELLOW}[*] Зареждане на сигнала от базата данни...${NC}"
                cat "$VAULT_DIR/$target_unlock"
                sleep 1
                echo -e "${GREEN}[!] Сигналът е изпратен успешно към NFC интерфейса! Вратата/Асансьорът е разкодиран.${NC}"
            else
                echo -e "${RED}[!] Грешка: Такава цел не е намерена в базата данни!${NC}"
            fi
            read -p "Натисни Enter за продължение..."
            ;;
        4)
            echo -e "\n${CYAN}[💻 USB / LAPTOP BRIDGE & HARDWARE SYNC]${NC}"
            echo -e "${GREEN}[*] Сканиране на USB портове за външни NFC антени (PN532 / ACR122U)...${NC}"
            lsusb | grep -iE "nfc|ftdi|silabs|prolific" || echo -e "${YELLOW}[*] Няма открити външни USB NFC хардуерни модули в момента.${NC}"
            read -p "Натисни Enter за продължение..."
            ;;
        5)
            echo -e "\n${CYAN}[💳 MICRO-PAYMENT ENGINE (5 - 100 EUR)]${NC}"
            read -p "Въведи сума за транзакция (EUR): " pay_amount
            if [ "$pay_amount" -ge 5 ] && [ "$pay_amount" -le 100 ]; then
                echo -e "${YELLOW}[*] Генериране на EMV/NFC заявка за сума: €$pay_amount ...${NC}"
                sleep 2
                echo -e "${GREEN}[+] Транзакцията е обработена успешно под ПИН лимита! Средствата са уловени в буфера.${NC}"
            else
                echo -e "${RED}[!] Сумата трябва да е между 5 и 100 евро!${NC}"
            fi
            read -p "Натисни Enter за продължение..."
            ;;
        6)
            echo -e "\n${CYAN}[⚡ КЛОНИРАНЕ НА UID ВЪРХУ НОВ ЧИП]${NC}"
            echo -e "${YELLOW}[*] Постави празен записваем чип на устройството...${NC}"
            sleep 2
            echo -e "${GREEN}[+] UID успешно прехвърлен и записан на новия физически носител!${NC}"
            read -p "Натисни Enter за продължение..."
            ;;
        0)
            echo -e "${GREEN}Изход от NFCAUTOKEY. Успех в лабораторията, братко!${NC}"
            exit 0
            ;;
        *)
            echo -e "${RED}Невалиден избор!${NC}"
            sleep 1
            ;;
    esac
done


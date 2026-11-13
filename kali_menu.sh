#!/bin/bash
while true; do
clear
echo -e "\e[1;31m"
cat << "EOF_BANNER"
    ___  ___  ___  _   _  ___  ______ _____ ______        ___  _ 
    |  \/  | / _ \ | | | |/ _ \ |  _  \  _  || ___ \      / _ \(_)
    | .  . |/ /_\ \| | | / /_\ \| | | | | | || |_/ /_____/ /_\ \_ 
    | |\/| ||  _  || | | |  _  || | | | | | ||  __/______|  _  | |
    | |  | || | | |\ \_/ / | | || |/ /\ \_/ /| |         | | | | |
    \_|  |_/\_| |_/ \___/\_| |_/|___/  \___/ \_|         \_| |_/_|
EOF_BANNER

echo "                 uu575198575198575198575198575198                  "
echo "              uu575198575198575198575198575198575198575198575198   "
echo "             u575198575198575198575198575198575198575198575198575198"
echo "            u575198575198575198\"   \"575198$\"   \"575198575198u"
echo "            \"575198575198\"      u       575198575198\""
echo "             575198       u        u575198$"
echo "             575198      :@       u575198$"
echo "              \"575198575198uuς  @@@  ςuu575198575198\""
echo "               \"575198575198575198575198@575198575198575198\""
echo "                    \"@@@@@@@@@\"                   "
echo -e "\e[1;36m"
echo "================================================================="
echo "       MARAUDER-AI QUANTIUM CYBERKILLER 8.4 GEMINI/ARGON-OLAMA    "
echo "================================================================="
echo -e "\e[1;33m--- OSNOVNI 30 INSTRUMENTA NA KALI LINUX (ROOT MODE) ---\e[0m\n"

echo -e "\e[1;32m 1.\e[0m Nmap (Network & Port Scanner)"
echo -e "\e[1;32m 2.\e[0m Masscan (Ultra-fast Port Scanner)"
echo -e "\e[1;32m 3.\e[0m Metasploit Framework (Exploitation)"
echo -e "\e[1;32m 4.\e[0m Burp Suite (Web Traffic Interception)"
echo -e "\e[1;32m 5.\e[0m Sqlmap (SQL Injection Automation)"
echo -e "\e[1;32m 6.\e[0m Wireshark (Network Packet Analyzer)"
echo -e "\e[1;32m 7.\e[0m Aircrack-ng (Wireless Security Auditor)"
echo -e "\e[1;32m 8.\e[0m Hydra (Password Cracking Tool)"
echo -e "\e[1;32m 9.\e[0m John the Ripper (Password Hash Cracker)"
echo -e "\e[1;32m10.\e[0m Nikto (Web Server Vulnerability Scanner)"
echo -e "\e[1;32m11.\e[0m Gobuster (Directory/File Bruteforcer)"
echo -e "\e[1;32m12.\e[0m Dirb (URL/Web Path Scanner)"
echo -e "\e[1;32m13.\e[0m Hashcat (Advanced Password Cracker)"
echo -e "\e[1;32m14.\e[0m Searchsploit (Exploit-DB Search Tool)"
echo -e "\e[1;32m15.\e[0m Sqlsus (MySQL Injection & Tampering)"
echo -e "\e[1;32m16.\e[0m Netcat (Networking & Backdoor Swiss Army Knife)"
echo -e "\e[1;32m17.\e[0m Tcpdump (Command-line Packet Analyzer)"
echo -e "\e[1;32m18.\e[0m Macchanger (MAC Address Spoofing)"
echo -e "\e[1;32m19.\e[0m Bettercap (Network Attack & Monitoring)"
echo -e "\e[1;32m20.\e[0m Responder (LLMNR/NBT-NS Poisoner)"
echo -e "\e[1;32m21.\e[0m Impacket (Network Protocols & Lateral Movement)"
echo -e "\e[1;32m22.\e[0m Binwalk (Firmware Analysis & Extraction)"
echo -e "\e[1;32m23.\e[0m Steghide (Steganography Hidden Data Extractor)"
echo -e "\e[1;32m24.\e[0m Ghidra (Reverse Engineering & Decompiler)"
echo -e "\e[1;32m25.\e[0m Medusa (Login Brute-forcer)"
echo -e "\e[1;32m26.\e[0m Kismet (GPS & Wireless Sniffer)"
echo -e "\e[1;32m27.\e[0m GQRX (Software Defined Radio / SDR)"
echo -e "\e[1;32m28.\e[0m Proxychains (Anonymity & Traffic Tunneling)"
echo -e "\e[1;32m29.\e[0m Whois (Domain & IP Information Lookup)"
echo -e "\e[1;31m30. Exit Menu\n\e[0m"

read -p "root@admiralerror:~# izberi instrument (1-30): " choice

case $choice in
    1)
        read -p "Vavedete IP ili Celta za Nmap scan: " target
        nmap -A -T4 $target
        ;;
    2)
        read -p "Vavedete IP/Range za Masscan: " target
        masscan $target -p1-65535 --rate=1000
        ;;
    3)
        msfconsole
        ;;
    4)
        burpsuite &
        ;;
    5)
        read -p "Vavedete URL za Sqlmap: " target
        sqlmap -u "$target" --batch --dbs
        ;;
    6)
        wireshark &
        ;;
    7)
        aircrack-ng
        ;;
    8)
        hydra
        ;;
    9)
        john
        ;;
    10)
        read -p "Vavedete URL za Nikto: " target
        nikto -h "$target"
        ;;
    11)
        read -p "Vavedete URL za Gobuster: " target
        gobuster dir -u "$target" -w /usr/share/wordlists/dirb/common.txt
        ;;
    12)
        read -p "Vavedete URL za Dirb: " target
        dirb "$target"
        ;;
    13)
        hashcat --help
        ;;
    14)
        read -p "Tarsene v Searchsploit (primer: apache): " query
        searchsploit "$query"
        ;;
    15)
        sqlsus
        ;;
    16)
        nc -h
        ;;
    17)
        tcpdump -i any
        ;;
    18)
        macchanger -s eth0
        ;;
    19)
        bettercap
        ;;
    20)
        responder -I eth0
        ;;
    21)
        python3 -m impacket
        ;;
    22)
        binwalk
        ;;
    23)
        steghide
        ;;
    24)
        ghidra &
        ;;
    25)
        medusa
        ;;
    26)
        kismet
        ;;
    27)
        gqrx &
        ;;
    28)
        read -p "Vavedete komanda za izpulnenie prez Proxychains: " cmd
        proxychains $cmd
        ;;
    29)
        read -p "Vavedete Domen/IP za Whois: " target
        whois "$target"
        ;;
    30)
        echo "Izhod ot menuto..."
        break
        ;;
    *)
        echo "Greshna opciq!"
        ;;
esac
read -p "Natisknete Enter za da se vurnete v menuto..."
done

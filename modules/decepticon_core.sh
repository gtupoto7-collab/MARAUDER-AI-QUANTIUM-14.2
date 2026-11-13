#!/bin/bash
clear
echo -e "\e[1;31m==================================================\e[0m"
echo -e "\e[1;33m       DECEPTICON CORE // OMNI-SCALE MATRIX        \e[0m"
echo -e "\e[1;31m==================================================\e[0m"
echo -e "\e[1;32m[*] Status: Decepticon protocols online.\e[0m"
echo -e "\e[1;32m[*] Core Intelligence: Llama 3.2 (Decepticon Mode)\e[0m\n"

# Proverka na Ollama i podgotovka na svarm-sredata
pgrep ollama >/dev/null || nohup ollama serve >/dev/null 2>&1 &
echo "[+] Matrix engine is fully loaded and primed."

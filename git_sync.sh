#!/bin/bash
echo "[+] Инициализиране на квантовото качване за BOOMKILLSHOT..."
if [ ! -d ".git" ]; then
    git init
    git branch -M main
fi
git add .
COMMIT_MSG="${1:-"Quantum core update: $(date +'%Y-%m-%d %H:%M:%S')"}"
git commit -m "$COMMIT_MSG"
git push -u origin main
if [ $? -eq 0 ]; then
    echo "[+] Квантовият модул BOOMKILLSHOT е успешно качен и регистриран в Git!"
else
    echo "[!] Грешка: Липсва отдалечено хранилище (origin) или достъп."
fi

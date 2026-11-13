adb logcat -s NfcService NfcDispatcher nfc_hal Tag | while read line; do
    if echo "$line" | grep -qE "Tag detected|UID|tagId|mUid|Protocol"; then
        TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
        LOG_ENTRY="[$TIMESTAMP] $line"
        
        # Izprashtane na danite kum lokalniya Node.js Express server
        curl -s -X POST "http://localhost:3000/api/nfc-tag" \
            -H "Content-Type: application/json" \
            -d "{\"logEntry\": \"$LOG_ENTRY\", \"timestamp\": \"$TIMESTAMP\"}" > /dev/null
            
        echo "[+] Prateno kum Node.js server za obrabotka i plashtane!"
    fi
done

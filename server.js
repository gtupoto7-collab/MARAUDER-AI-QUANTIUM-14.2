const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

// Endpoint za prijemane na plashtaniya / webhooks ot Telegram Stars
app.post('/webhook/telegram', (req, res) => {
    console.log('[+] Poluchen webhook ot Telegram:', req.body);
    // Tuk shte obrabotvame uspehnite plashtaniya (pre_checkout_query / successful_payment)
    res.status(200).send('OK');
});

// Endpoint za proverka na statusa na NFC vault-a
app.get('/vault/status', (req, res) => {
    res.json({ status: 'SECURE', brand: 'MARAUDER-AL', active: true });
});

app.listen(PORT, () => {
    console.log(`[+] MARAUDER-AL Payment & Vault Server e pusnat na port ${PORT}`);
});

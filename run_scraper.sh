#!/bin/bash
cd /mnt/c/Users/gtupo/darkwebarmy_lab
./venv/bin/python3 extract_news.py >> cron_execution.log 2>&1

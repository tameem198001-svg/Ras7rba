"""
telegram_bot.py
Template to send a daily message with the last ledger entry.
"""
import os
import json
import sqlite3

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')


def last_pulse_summary(db='noor_wall_ledger.db'):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT created_at, simulation_name, result_checksum FROM ledger ORDER BY id DESC LIMIT 1')
    r = cur.fetchone()
    conn.close()
    if not r:
        return 'No pulses yet.'
    return f"{r[0]} - {r[1]} (checksum {r[2][:8]})"


def send_telegram(message):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        raise RuntimeError('Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID environment variables')
    import requests
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    requests.post(url, json={'chat_id': CHAT_ID, 'text': message})


if __name__ == '__main__':
    msg = last_pulse_summary()
    print(msg)
    # send_telegram(msg)

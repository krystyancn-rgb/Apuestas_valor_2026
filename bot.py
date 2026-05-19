import requests
import os

TOKEN = "AAG-tVM3PFVjxapQTdYRjD2yvGTCKcmqnKo"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send_message(chat_id, text):
    requests.post(URL, data={
        "chat_id": chat_id,
        "text": text
    })

def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    return requests.get(url).json()

def main():
    print("Bot iniciado")

    data = get_updates()

    if data.get("result"):
        for update in data["result"]:
            if "message" in update:
                chat_id = update["message"]["chat"]["id"]

                send_message(chat_id, "👋 Bot activo. Funciona correctamente en Render.")

if __name__ == "__main__":
    main()

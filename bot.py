import requests
import time

TOKEN = tVM3PFVjxapQTdYRjD2yvGTCKcmqnKo
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

CHAT_ID = None


def send_message(chat_id, text):
    requests.get(URL, params={"chat_id": chat_id, "text": text})


def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    return requests.get(url).json()


def main():
    global CHAT_ID

    print("Bot iniciado...")

    while True:
        data = get_updates()

        if data.get("result"):
            for update in data["result"]:
                if "message" in update:
                    CHAT_ID = update["message"]["chat"]["id"]

                    send_message(CHAT_ID, "👋 Bot ValueBet activo. Funcionando correctamente.")

        time.sleep(5)


if __name__ == "__main__":
    main()

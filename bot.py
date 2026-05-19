import requests
import time

TOKEN = "AAG-tVM3PFVjxapQTdYRjD2yvGTCKcmqnKo"
URL = f"https://api.telegram.org/bot{TOKEN}"

def send_message(chat_id, text):
    requests.post(f"{URL}/sendMessage", data={
        "chat_id": chat_id,
        "text": text
    })

def get_updates(offset=None):
    params = {"timeout": 10}
    if offset:
        params["offset"] = offset

    try:
        r = requests.get(f"{URL}/getUpdates", params=params, timeout=15)
        return r.json()
    except:
        return {"result": []}

def main():
    print("Bot iniciado")
    offset = None

    while True:
        data = get_updates(offset)

        for update in data.get("result", []):
            offset = update["update_id"] + 1

            if "message" in update:
                chat_id = update["message"]["chat"]["id"]
                text = update["message"].get("text", "")

                print("Mensaje:", text)

                send_message(chat_id, "👋 Bot activo en Render")

        time.sleep(2)

if __name__ == "__main__":
    main()

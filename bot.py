import requests
import time

TOKEN = "AAGPZzvHNg-n2lVHgaEQUFxTRfdb8R8gcyc"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

def send_message(chat_id, text):
    requests.post(
        f"{BASE_URL}/sendMessage",
        data={"chat_id": chat_id, "text": text},
        timeout=10
    )

def get_updates(offset=None):
    params = {
        "timeout": 10
    }

    if offset is not None:
        params["offset"] = offset

    response = requests.get(
        f"{BASE_URL}/getUpdates",
        params=params,
        timeout=15
    )

    return response.json()

def main():
    print("Bot iniciado")

    # Leer actualizaciones antiguas y descartarlas
    data = get_updates()
    offset = None

    if data.get("result"):
        offset = data["result"][-1]["update_id"] + 1

    print("Esperando mensajes nuevos...")

    while True:
        try:
            data = get_updates(offset)

            for update in data.get("result", []):
                offset = update["update_id"] + 1

                if "message" in update:
                    chat_id = update["message"]["chat"]["id"]
                    text = update["message"].get("text", "")

                    print(f"Mensaje recibido: {text}")

                    send_message(
                        chat_id,
                        "👋 ¡Hola! El bot ya funciona correctamente."
                    )

            time.sleep(1)

        except Exception as e:
            print("Error:", e)
            time.sleep(5)

if __name__ == "__main__":
    main()

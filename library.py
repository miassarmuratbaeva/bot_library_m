import requests

class Library:
    def __init__(self, token):
        self.token=token
        self.api_url = f"https://api.telegram.org/bot{token}/"

    def get_updates(self, offset=None):
        url = self.api_url + "getUpdates"
        params = {"offset": offset, "timeout": 30}
        response = requests.get(url, params=params)
        return response.json().get("result", [])

    def send_message(self, chat_id, text):
        url = self.api_url + "sendMessage"
        data = {"chat_id": chat_id, "text": text}
        requests.post(url, data=data)
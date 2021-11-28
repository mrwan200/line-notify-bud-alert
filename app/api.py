import requests

class LINENotifyAPI:
    URL = "https://notify-api.line.me/api/notify"

    def __init__(self, key) -> None:
        self.apikey = key
        

    def send(self, message):
        return requests.post(
            self.URL,
            headers=self.__headers(),
            data={
                "message": message
            }
        )

    def __headers(self):
        return {
            "Authorization":  f"Bearer {self.apikey}"
        }
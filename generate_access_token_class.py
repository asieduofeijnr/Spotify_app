import requests


class GetAccess:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        pass

    def generate(self):
        auth_response = requests.post(
            "https://accounts.spotify.com/api/token",
            {
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
        )
        auth_response_data = auth_response.json()
        auth_response_data = auth_response_data["access_token"]

        return auth_response_data

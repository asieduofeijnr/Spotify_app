from generate_access_token_class import requests


class Search:
    def __init__(self, headers, BASE_URL):
        self.headers = headers
        self.base_url = BASE_URL

    def generate(self, search_query):
        r = requests.get(
            self.base_url + "search",
            headers=self.headers,
            params={"q": search_query, "type": "artist"},
        )

        r = r.json()["artists"]["items"]
        search_result = [
            {
                "artist_name": search["name"],
                "artist_id": search["id"],
                "artist_image": "https://www.shoshinsha-design.com/wp-content/uploads/2020/05/noimage-760x460.png"
                if search["images"] == []
                else search["images"][0]["url"],
            }
            for search in r
        ]

        return search_result

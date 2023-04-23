from search_class import Search, requests


class Artist(Search):
    def name(self, artist_id):
        r = requests.get(self.base_url + "artists/" + artist_id, headers=self.headers)
        r = r.json()
        return r["name"]

    def url(self, artist_id):
        r = requests.get(self.base_url + "artists/" + artist_id, headers=self.headers)
        r = r.json()
        return r["external_urls"]["spotify"]

    def followers(self, artist_id):
        r = requests.get(self.base_url + "artists/" + artist_id, headers=self.headers)
        r = r.json()
        return r["followers"]["total"]

    def image(self, artist_id):
        r = requests.get(self.base_url + "artists/" + artist_id, headers=self.headers)
        r = r.json()
        return r["images"][0]["url"]

    def populartiy(self, artist_id):
        r = requests.get(self.base_url + "artists/" + artist_id, headers=self.headers)
        r = r.json()
        return r["popularity"]

    def artist_audio_features(self, artist_ID):
        r = requests.get(
            self.base_url + "artists/" + artist_ID + "/albums",
            headers=self.headers,
            params={"include_groups": "album"},
        )
        artist_albums = r.json()

        data = []
        # pull all albums(No duplicates)
        album_nameid = {album["name"]: album["id"] for album in artist_albums["items"]}

        # get tracks from album using album ids
        for album in album_nameid:
            r = requests.get(
                self.base_url + "albums/" + album_nameid[album] + "/tracks",
                headers=self.headers,
            )

            tracks = r.json()["items"]

            # get audio features from each track from each album
            for track in tracks:
                f = requests.get(
                    self.base_url + "audio-features/" + track["id"],
                    headers=self.headers,
                )
                f = f.json()

                # update the audio feature dictionary with the track name and album name
                f.update(
                    {
                        "track_name": track["name"],
                        "album_name": album,
                        "artist_name": track["artists"][0]["name"],
                    }
                )
                data.append(f)
        return data

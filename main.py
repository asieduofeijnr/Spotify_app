import streamlit as st
import pandas as pd
import plotly.express as px

from search_class import Search
from artist_class import Artist
from config import spotify_client_id, spotify_client_secret
from generate_access_token_class import GetAccess
from streamlit_star_rating import st_star_rating
from time import sleep

import pandas as pd
from stqdm import stqdm

stqdm.pandas()


###################################################################################
# Get access token from spotify
access_token = GetAccess(spotify_client_id, spotify_client_secret)
ACCESS_TOKEN = access_token.generate()

# Access token header for every query or requst
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
BASE_URL = "https://api.spotify.com/v1/"

# Create instance of Search
artist_list = Search(headers, BASE_URL)
###################################################################################


# Streamlit Page
st.set_page_config(
    page_title="Artist Songs Analyser", page_icon=":musical_note:", layout="wide"
)
st.title(
    "Welcome to my Spotify Artist Songs Analyser :musical_note::chart_with_upwards_trend:"
)
st.subheader(
    "So firsts things first, lets search for your favorite artist below :singer:."
)

search_query = st.text_input(label=" ", placeholder="Type your artist name")
submitted = st.button("Lets see what we got")

# Get Artist seach query and display to the user
if submitted:
    try:
        artist_details = artist_list.generate(search_query)

        artist_names = [artist["artist_name"] for artist in artist_details]
        artist_ids = [artist["artist_id"] for artist in artist_details]
        artist_images = [artist["artist_image"] for artist in artist_details]

        # create a 4 column grid
        col1, col2, col3, col4 = st.columns(4)

        for i in range(len(artist_names)):
            if i % 4 == 0:
                cell = col1
            elif i % 4 == 1:
                cell = col2
            elif i % 4 == 2:
                cell = col3
            else:
                cell = col4

            cell.image(artist_images[i], width=100)
            cell.button(artist_names[i], key=artist_ids[i])

    except KeyError:
        st.error("Oops!! Did you forget your artist name")


artist_id = [
    artist_ids
    for artist_ids in st.session_state
    if st.session_state[artist_ids] == True
]


# Create an instance of artist by inheriting Search __init__
artist = Artist(headers, BASE_URL)

if artist_id:
    artist_id = artist_id[0]

    artist_name = artist.name(artist_id)
    artist_url = artist.url(artist_id)
    artist_followers = artist.followers(artist_id)
    artist_image = artist.image(artist_id)
    artist_popularity = artist.populartiy(artist_id)

    st.image(artist_image, width=200)
    st.title(f"Artist: {artist_name}")
    st.subheader(f"Artist Spotify Url : {artist_url}")
    st.subheader(f"Artist Followers : {format(artist_followers, ',')}")
    st.subheader(f"Popularity : {artist_popularity}")
    stars = st_star_rating(
        label=None,
        maxValue=5,
        defaultValue=0.05 * artist_popularity,
        key="rating",
        read_only=True,
    )
    st.subheader(
        f"Below is the dataframe (table) of all audio-features of {artist_name}'s tracks"
    )

if artist_id:
    with st.spinner("Loading data....Please Wait"):
        data = artist.artist_audio_features(artist_id)
        df = pd.DataFrame(data)

        fields = [
            "album_name",
            "track_name",
            "duration_ms",
            "danceability",
            "energy",
            "key",
            "loudness",
            "acousticness",
            "instrumentalness",
            "liveness",
            "valence",
            "tempo",
        ]

        df = df.reindex(columns=fields)
        df = df.rename(str.capitalize, axis="columns")

        st.dataframe(df)
    st.success("Data Loaded", icon="🤖")

if artist_id:
    st.subheader("Now lets look at some charts :smile:")

    st.write(
        f"A scatter plot of ACOUSTICNESS TO VALENCE(HOW SAD :cry: OR HAPPY :smile:) based on {artist_name}'s albums"
    )

    x = "Valence"
    y = "Acousticness"
    size = "Danceability"

    fig = px.scatter(
        df, x=x, y=y, size=size, color="Album_name", hover_name="Track_name"
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

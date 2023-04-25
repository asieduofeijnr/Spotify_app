# Spotify Artist Analyser Python Web App
This is a Python web application that allows you to analyse the audio features of songs by your favorite artist on Spotify. The application provides a scatter plot of the acousticness to valence (how sad or happy) based on the artist's albums and a detailed analysis of the artist's audio features.

# Requirements
Python 3.6 or higher <br>
pandas <br>
streamlit <br>
plotly.express

# How to use the app
Clone this repository to your local machine. Dont forget to get your API Keys <br>
Open your terminal and navigate to the directory where you cloned the repository. <br>
Run the command streamlit run app.py to launch the app in your browser. <br>
Once the app is launched, you will be able to search for your favorite artist by typing their name in the text box and clicking the "Let's see what we got" button. <br>
After selecting your artist, the application will load their data, and you will see a scatter plot of the acousticness to valence based on their albums and a summary of the analysis.

# Screenshot of the app in action

## Displaying the dataframe of the artist
![First](https://user-images.githubusercontent.com/114332208/231563235-2a997288-ea25-4c3f-b16d-620bfb7cdd75.png)

## Displaying the Graph of the set axis
![Chart](https://user-images.githubusercontent.com/114332208/231563292-63d68cc1-6128-4ede-a4f0-ce5aeb786ba4.png)

## Chat GPT in action analysing the chart
![Chat Gpt](https://user-images.githubusercontent.com/114332208/231563318-0c5b0f0d-9a93-43f1-b21a-4b578ba38247.png)



# Acknowledgments
This app was created using the Spotify Web API, OpenAi ChatGPT 3 API and the Streamlit Python library.



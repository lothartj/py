from pytube import YouTube
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def download_video():
    if request.method == 'POST':
        # Get the YouTube video URL from the form
        video_url = request.form['url']

        # Create a YouTube object with the provided URL
        yt = YouTube(video_url)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Prompt the user to specify the download path
        download_path = request.form['path']

        # Download the video
        stream.download(output_path=download_path)
        return "Download completed!"

    # HTML form
    return '''
        <form method="POST"><center>
            <label for="url">YouTube Video URL:</label><br>
            <input type="text" id="url" name="url" required><br><br>
            <label for="path">Download Path:</label><br>
            <input type="text" id="path" name="path" required><br><br>
            <input type="submit" value="Download"><center>
        </form>
    '''

if __name__ == '__main__':
    app.run()

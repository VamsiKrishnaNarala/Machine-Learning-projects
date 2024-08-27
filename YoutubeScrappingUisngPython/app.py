from pytube import YouTube
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/WebScrapping', methods=['POST','GET'])
def WebScrapping():
    youtubelink= str(request.form['url'])
    link=str(youtubelink)
    yt = YouTube(link)
    a=yt.description
    # stream = yt.streams.get_highest_resolution()
    # stream.download()
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    f= soup.find('meta', {'name': 'description'})['content']

    return render_template('index.html',Title=yt.title, Description =f,Views=yt.views)
    
if __name__ == '__main__':
    app.run(debug=True)

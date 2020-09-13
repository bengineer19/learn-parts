import os
from flask import (
    Flask, render_template, request, redirect, jsonify, send_file
)
from dotenv import load_dotenv
# Load env vars before any import which need them to set up 
load_dotenv(os.path.join(os.getcwd(), '.env'))

from gdrive import get_song, get_file


app = Flask(__name__)


@app.route('/')
def home():
    return 'Homepage'


@app.route('/song/<folder_id>')
def song_page(folder_id):
    song = get_song(folder_id)
    return render_template("song.html", song=song)


@app.route('/audio/<file_id>')
def get_mp3(file_id):
    return send_file(
        get_file(file_id),
        as_attachment=True,
        attachment_filename=f'{file_id}.mp3',
        mimetype='audio/mpeg'
    )
import os
from flask import (
    Flask, render_template, request, redirect, jsonify, send_file
)
from dotenv import load_dotenv
# Load env vars before any import which need them to set up 
load_dotenv(os.path.join(os.getcwd(), '.env'))

from gdrive import get_song, get_file, get_show


app = Flask(__name__)


@app.route('/')
def home():
    return 'Get in touch with me (Ben James - bwj23@cam.ac.uk) for usage instructions, to give feedback, or anything at all!'


@app.route('/song/<folder_id>')
def song_page(folder_id):
    song = get_song(folder_id)
    return render_template("song.html", song=song, title=song['title'])


@app.route('/show/<folder_id>')
def show_page(folder_id):
    show = get_show(folder_id)
    return render_template("show.html", show=show, title='Show listing')


@app.route('/audio/<file_id>')
def get_mp3(file_id):
    return send_file(
        get_file(file_id),
        as_attachment=True,
        attachment_filename=f'{file_id}.mp3',
        mimetype='audio/mpeg'
    )

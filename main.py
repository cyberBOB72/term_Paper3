from utils import *
from flask import Flask, render_template, request

posts = get_posts_all('data\posts.json')

app = Flask(__name__)


@app.route("/")
def page_index():
    post = posts
    return render_template('index.html', post=post)

app.run()
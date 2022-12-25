from utils import *
from flask import Flask, render_template, request

posts = get_json('data\posts.json')
comments = get_json('data\comments.json')

app = Flask(__name__)


@app.route("/")
def page_index():
    post = posts
    return render_template('index.html', post=post)


@app.route("/posts/<int:postid>")
def page_post(postid):
    post = get_posts_by_user(postid, posts)
    comment = get_comments_by_post_id(postid, comments)
    return render_template('post.html', post=post, comment=comment, count=len(comment))



app.run()

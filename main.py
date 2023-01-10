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
    post = get_posts_by_pk(postid, posts)
    comment = get_comments_by_post_id(postid, comments)
    return render_template('post.html', post=post, comment=comment, count=len(comment))


@app.route("/search/", methods=["POST"])
def page_search():
    name = request.values.get('name')
    post = search_for_posts(name, posts)
    return render_template('search.html', post=post, count=len(post))


@app.route("/users/<username>")
def page_user(username):
    post = get_posts_by_user(username, posts)
    return render_template('user-feed.html', post=post)


@app.errorhandler(404)
def not_found(e):
    return "<h1>404</h1><p>Такой страницы нет</p>"


@app.errorhandler(500)
def not_found(e):
    return "<h1>500</h1><p>Сервер устал и спит</p>"


app.run()

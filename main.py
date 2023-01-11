import logging

from utils import *
from flask import Flask, render_template, request, jsonify

posts = get_json('data\posts.json')
comments = get_json('data\comments.json')

logger_one = logging.getLogger("logs/api.log.txt")
file_handler = logging.FileHandler("logs/api.log.txt")
formatter = logging.Formatter("%(asctime)s : [%(levelname)s] : %(message)s")
file_handler.setFormatter(formatter)
logger_one.addHandler(file_handler)

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
    comment = get_comments_by_post_id(username, comments)
    return render_template('user-feed.html', post=post, comment=comment, count=len(comment))


@app.errorhandler(404)
def not_found(e):
    return "<h1>404</h1><p>Такой страницы нет</p>"


@app.errorhandler(500)
def not_found(e):
    return "<h1>500</h1><p>Сервер устал и спит</p>"


@app.route("/api/posts")
def get_posts():
    logging.info("Посты запрошены")
    post = posts
    return jsonify(post)


@app.route("/api/posts/<int:post_id>")
def get_post(post_id):
    logging.info("Определенный пост запрошен")
    post = get_posts_by_pk(post_id, posts)
    return jsonify(post)


app.run()

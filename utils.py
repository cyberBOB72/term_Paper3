import json
from json import JSONDecodeError


def get_posts_all(data):
    """
    Возвращает посты
    :return: json.load(file)
    """
    try:
        with open(data, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл не найден")
    except JSONDecodeError:
        print("Файл не удается преобразовать")


def get_posts_by_user(user_name, data):
    """
    Посты определенного пользователя
    :param user_name: None
    :return:
    """
    try:
        for name in data:
            if user_name == name['poster_name']:
                return name
    except ValueError:
        return f'Такого пользователя нет'


def get_comments_by_post_id(post_id, data):
    """
    Возвращает комментарии определенного поста
    """
    try:
        with open(data, 'r', encoding='utf-8') as file:
            comments = json.load(file)
    except FileNotFoundError:
        print("Файл не найден")
    except JSONDecodeError:
        print("Файл не удается преобразовать")
    try:
        all_comments = []
        for comment in comments:
            if post_id == comment['post_id']:
                all_comments.append(comment['comment'])
        return all_comments
    except ValueError:
        return f'Такого поста нет'


def search_for_posts(query, data):
    """
    Возвращает список постов по ключевому слову
    """
    posts = []
    for post in data:
        if query in post['content']:
            posts.append(post)
    return posts


def get_post_by_pk(pk, data):
    """
    Возвращает один пост по его идентификатору
    """
    for id in data:
        if pk == id['pk']:
            return id

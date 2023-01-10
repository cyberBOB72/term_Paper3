import json
from json import JSONDecodeError


def get_json(data):
    """
    Чтение фалов json.
    :return: json.load(file)
    """
    try:
        with open(data, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл не найден")
    except JSONDecodeError:
        print("Файл не удается преобразовать")


def get_posts_by_pk(pk, data):
    """
    Посты определенного пользователя
    :param user_name: None
    :return:
    """
    try:
        for name in data:
            if pk == name['pk']:
                return name
    except ValueError:
        return f'Такого пользователя нет'

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
    all_comments = []
    try:
        for name in data:
            if post_id == name['post_id']:
                all_comments.append(name)
        return all_comments
    except ValueError:
        return f'Такого поста нет'


def search_for_posts(query, data):
    """
    Возвращает список постов по ключевому слову
    """
    posts = []
    for post in data:
        if query.lower() in post['content'].lower():
            posts.append(post)
    return posts[:10]


def get_post_by_pk(pk, data):
    """
    Возвращает один пост по его идентификатору
    """
    for id in data:
        if pk == id['pk']:
            return id

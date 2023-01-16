import json


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
    except json.JSONDecodeError:
        print("Файл не удается преобразовать")


def get_posts_by_pk(pk, data):
    """
    Пост определенного пользователя
    :param pk: None
    :return:
    """
    try:
        for name in data:
            if pk == name['pk']:
                return name
    except:
        return f'Такого пользователя нет'

def get_posts_by_user(user_name, data):
    """
    Пост определенного пользователя
    :param user_name: None
    :return:
    """
    try:
        for name in data:
            if user_name == name['poster_name']:
                return name
    except:
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

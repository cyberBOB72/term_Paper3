import json

def get_posts_all(data):
    """
    Возвращает посты
    :return: json.load(file)
    """
    with open(data, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name, data):
    """
    Посты определенного пользователя
    :param user_name: None
    :return:
    """
    try:
        for name in data:
            if user_name == name['poster_name']:
                return name #??
        return 'Not Found'
    except ValueError:
        print('Такого пользователя нет')

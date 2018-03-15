import requests


class AvatarNotFoundException(BaseException):
    pass


def avatar(usuario):
    """Retorna o link com avatar do usuário
    :param usuario: str com nome do usuario
    :return: str
    """

    try:
        r = requests.get(f'https://api.github.com/users/{usuario}')
        return r.json()['avatar_url']
    except Exception as err:
        print(err)
        raise AvatarNotFoundException()


if __name__ == '__main__':
    try:
        print(avatar('renzon'))
    except AvatarNotFoundException:
        print("Avatar não encontrado.")

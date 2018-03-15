import requests


def avatar(usuario):
    """Retorna o link com avatar do usuário
    :param usuario: str com nome do usuario
    :return: str
    """

    resposta = ""
    try:
        resp = requests.get(f'https://api.github.com/users/{usuario}')
        resposta = resp.json()['avatar_url']
    except KeyError:
        resposta = "Não encontrado"

    return resposta


if __name__ == '__main__':
    print(avatar('fredericoaraujo'))
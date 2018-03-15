"""
Criar um pacote para obtenção de dados de um XML
Instalar a lib requests para fazer o download do arquivo
Utilizar a lib xmltodict
Criar uma função que retorne a lista de titulos dos CDs
Link: http://www.w3schools.com/xml/cd_catalog.xml
Instalar o flake8
Configurar o travis e rodar flake8
"""

import requests
import xmltodict


def download_arquivo(url):
    r = requests.get(url)
    return r.content


def get_lista_titulo(str_xml):
    xml_to_dct = dict(xmltodict.parse(str_xml))
    catalog = xml_to_dct['CATALOG']
    dct_cds = catalog['CD']
    list_titles = []
    for cd in dct_cds:
        list_titles.append(cd['TITLE'])

    return list_titles


if __name__ == '__main__':
    read_xml = download_arquivo('http://www.w3schools.com/xml/cd_catalog.xml')
    print(get_lista_titulo(read_xml))

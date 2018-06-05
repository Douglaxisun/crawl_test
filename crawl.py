# coding=utf-8

import requests
from bs4 import BeautifulSoup


# ��ȡhtml�ĵ�
def get_html(url):
    """get the content of the url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


# ��ȡЦ��
def get_certain_joke(html):
    """get the joke of the html"""
    soup = BeautifulSoup(html, 'lxml')
    joke_content = soup.select('div.content')[0].get_text()

    return joke_content


url_joke = "https://www.qiushibaike.com/hot/"
html = get_html(url_joke)
joke_content = get_certain_joke(html)
print joke_content
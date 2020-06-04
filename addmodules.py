from requests_html import HTMLSession
import re
from lxml import etree
import json
import os

def wb_pages_count(url_page):
    session = HTMLSession()
    resp = session.get(url_page)
    pages_ = resp.html.xpath('//span[@class="goods-count j-goods-count"]/text()')
    pages_ = pages_[0]
    pages_= pages_.replace("\\n","") # Удаляем переносы
    pages_ = pages_.replace('товара', '') #Удаляем слово товары
    pages_ = pages_.replace('товаров', '')  # Удаляем слово товары
    pages_ = (''.join(pages_.split())) # Удаляем лишние пробелы
    pages_= int(pages_)
    pages_ = pages_//100 + 1 # - число страниц выдачи
    print(f'{pages_} results page(s)')
    return pages_+1

if __name__ == "__main__":

    wb_pages_count('https://www.wildberries.ru/catalog/dlya-doma/predmety-religii/oberegi')



#
#
# # Чтение файла с ключами
# def read_file(file_name="keywords.txt"):
#     try:
#         with open(file_name) as f:
#             keywords = f.read().split('\n')
#             print(keywords)
#     except Exception as s:
#         print(f'Спарсить выдачу не удалось, ошибка - {s}')
#         keywords = None
#     return keywords
#
# # Чтение выдачи bing
#
# def bing_read(key):
#     links = []
#     titles = []
#     descriptions = []
#     session = HTMLSession()
#     print(f'Парсим "{key}"...')
#     try:
#         url = f'https://www.bing.com/search?q={key}'
#         print(url)
#         resp = session.get(url)
#         print(resp)
#
#         # links = resp.html.xpath('//li[@class='b_algo']//h2/a/@href')
#
#         # print(links)
#         titles_with_html=resp.html.xpath=("//li[@class='b_algo']//h2/a")
#         # print('resp2')
#         descriptions_with_html = resp.html.xpath("//ol[@id='b_results']/li//div/p")
#         # print('resp4')
#
#         for tit_with_html in titles_with_html:
#             print('resp3')
#             titles.append(tit_with_html)
#
#
#         for desc_with_html in descriptions_with_html:
#             descriptions.append(desc_with_html)
#
#     except Exception as s:
#         print(f'Спарсить выдачу не удалось. Ошибка{s}')
#         links = []
#         titles = []
#         descriptions = []
#     return(links, titles, descriptions)
# # For function tests
# if __name__ == "__main__":
#
# #
#     key = 'privet'
#     read_file()
#     bing_read('privet')
#

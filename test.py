from requests_html import HTMLSession
from selenium import webdriver
import time


import time
import json
import addmodules as am

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
driver = webdriver.Chrome()
driver.get("https://www.wildberries.ru/catalog/5109514/detail.aspx?targetUrl=MI")
time.sleep(0.001)
el_list = driver.find_elements_by_xpath('//span[@class="j-orders-count"]')
el_text = el_list[0].text
el_text = el_text.replace('Купили ', '')
el_text = el_text.replace('более ', '')
el_text = el_text.replace('менее ', '')
el_text = el_text.replace(' раза', '')
el_text = el_text.replace(' раз', '')
el_text = int(el_text)
print(type(el_text))
print(el_text)
driver.quit()

# url = 'https://www.wildberries.ru/catalog/5109514/detail.aspx?targetUrl=MI'
# session = HTMLSession()
#
# resp = session.get(url)
#


# time.sleep(2)
#
# brands_dim = resp.html.xpath('//span[@class="name"]/text()')
# count_dim = resp.html.xpath('//span[@class="j-orders-count"]/text()')
# print(count_dim)
# print(brands_dim)
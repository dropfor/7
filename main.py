from requests_html import HTMLSession
import time
import json
import addmodules as am
import re

session = HTMLSession()
url = 'https://www.wildberries.ru/catalog/muzhchinam/bele/noski'
count_pages = am.wb_pages_count(url)

# делаем массив страниц
pages_dim = []
for i in range(1,count_pages,1):
    pages_to = url + f'?page={i}'
    pages_dim.append(pages_to)

# загоняем список url товаров в массив
url_dim = []
j=0
for y in pages_dim:
    resp = session.get(y)

    full_url = resp.html.xpath('//div[@class="dtList-inner"]//a[@class="ref_goods_n_p j-open-full-product-card"]/@href')
    for z in full_url:
        url_dim.append(z)
        j = j + 1
        print(f'Adding .. {z} : {j}')

names = []
brands = []
count = []
price = []
stars = []

print(' Pages done. Start to get data ')



# # Парсим данные со страниц
#
j=0
data = []
for i in url_dim:


# webdriver
#     driver = webdriver.Chrome()
#     driver.get(url_dim[i])
#     # Count
#     count = driver.find_elements_by_xpath('//span[@class="j-orders-count"]')
#     print(count[0].text)
#     driver.quit()

    resp = session.get(i)
    resp.html.render()

# Купили
    count_text = resp.html.xpath('//span[@class="j-orders-count"]/text()')
    if len(count_text) > 0:
        count_text[0] = count_text[0].replace('Купили', '')
        count_text[0] = count_text[0].replace('более', '')
        count_text[0] = count_text[0].replace('менее', '')
        count_text[0] = count_text[0].replace('раза', '')
        count_text[0] = count_text[0].replace('раз', '')
    else:
        count_text.append('0')
# Бренды

    names_dim = resp.html.xpath('//span[@class="name"]/text()')
    brands_dim = resp.html.xpath('//span[@class="brand"]/text()')
    price_dim = resp.html.xpath('//span[@class="final-cost"]/text()')
    price_dim[0] = price_dim[0].replace('\n','')
    price_dim[0] = price_dim[0].replace(' ₽','')
    price_splitted = price_dim[0].split()
    if len(price_splitted) == 2:
        price_splitted[0]=price_splitted[0]+price_splitted[1]
    print(f'Adding {brands_dim[0]}/{names_dim[0]} - {price_splitted[0]} руб. куплено около {count_text[0]} раз')
    j = j + 1
    print(f'сделано {j}/осталось {len(url_dim)-j}')

    data.append({
        'url': i,
        'name' : names_dim[0],
        'brand': brands_dim[0],
        'price': price_splitted[0],
        'count': count_text[0]

    })

with open('noski_wb.json', 'w', encoding='utf-8') as fh:
     fh.write(json.dumps(data,ensure_ascii=False))

#
# #brands
# #chrome

# #requests
#     resp = session.get(i)
#     time.sleep(2)
#     names_dim = resp.html.xpath('//span[@class="brand"]/text()')
#     names.append(names_dim[0])
#
# #купили
#
#     el_list = driver.find_elements_by_xpath('//span[@class="j-orders-count"]')
#     el_text = el_list[0].text
#     el_text = el_text.replace('Купили ', '')
#     el_text = el_text.replace('более ', '')
#     el_text = el_text.replace('менее ', '')
#     el_text = el_text.replace(' раза', '')
#     el_text = el_text.replace(' раз', '')
#     el_text = int(el_text)
#     count.append(el_text)
#     driver.quit()
#
# #names
#     brands_dim = resp.html.xpath('//span[@class="name"]/text()')
#     brands.append(brands_dim[0])
#     print(f'Adding {names_dim[0]} - {brands_dim[0]}')
#
#     print(f'Adding {names_dim[0]} / {brands_dim[0]} /Купили {el_text}')
#
#
# #price
# #stars
#
#
#
#
# # print(url_dim)
# # print(len(url_dim))
# #
# # print(url)
# # resp = session.get(url)
# # print(resp)
# # # links = []
# # brand_names_= resp.html.xpath('//div[@class="dtList-inner"]//strong[@class="brand-name c-text-sm"]/text()'
# #                               '')
# # full_url = resp.html.xpath('//div[@class="dtList-inner"]//a[@class="ref_goods_n_p j-open-full-product-card"]/@href')
# # prod_names_= resp.html.xpath('//div[@class="dtlist-inner-brand"]//span[@class="goods-name c-text-sm"]/text()')
# # prices_actual_= resp.html.xpath('//div[@class="j-cataloger-price"]//ins[@class="lower-price"]/text()')
# # url_actual_= resp.html.xpath('//div[@class="item j-product-item lslide active"]//a/@href')
# # # for prices in price_actual_:
# #     # prices.replace('\xa','')
# #     # prices.replace('','')
# #
# #
# # wb_dics = list(zip(brand_names_, full_url))
# #
# # print(brand_names_)
# # print(len(brand_names_))
# # # print(url_actual_)
# # # print(len(url_actual_))
# # print(full_url)
# # print(len(full_url
# #           ))
# # print(wb_dics)
# # # print(prod_names_)
# # # print(len(prod_names_))
# # # print(prices_actual_)
# # # print(len(prices_actual_))
# #
# # with open('text.json', 'w', encoding='utf-8') as fh:
#     fh.write(json.dumps(wb_dics,ensure_ascii=False))
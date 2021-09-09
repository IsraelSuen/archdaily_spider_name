import requests
from bs4 import BeautifulSoup
import csv
import openpyxl

# res = requests.get('https://www.archdaily.cn/cn/page/')
# res = requests.get('https://www.baidu.com')
# print(res.status_code)
# print(type(res))
# print(res)

item_all = []

for x in range(15):
    res = requests.get('https://www.archdaily.cn/cn/page/' + str(x))
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(class_='afd-title--black-link')
    for item in items:
        name = item.text

        URL = 'https://www.archdaily.cn' + item['href']
        item_all.append([name, URL])

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.tittle = 'new tittle'
    print(item_all)

for i in item_all:
    sheet.append(i)

    wb.save('archdaily.xlsx')

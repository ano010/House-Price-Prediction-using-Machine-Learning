import requests as r
from bs4 import BeautifulSoup as bs
import pandas as pd
import os

def extractUrls(content):
    soup = bs(content)
    urlContainerList = soup.findAll('div', {'class': 'item-thumb'})
    urls = []
    for index in range(len(urlContainerList)):
       try:
            urlDom = urlContainerList[index].find_all('a')[0]['href']
       except IndexError:
           continue
       urls.append('https://ikman.lk' + urlDom)
    return urls


def getUrl(page):
    return 'https://ikman.lk/en/ads/colombo/houses?page=' + str(page) + '&type=for_sale'

def extractItem(content):
    arr = []
    headers = []
    soup = bs(content)
    try:
        itemTopElem = soup.findAll('div', { 'class': 'item-top'})[0]
    except IndexError:
        return -1
    # find title
    try:
        title = itemTopElem.find_all('h1')[0].text;
    except IndexError:
        return -1
    try:
        itemIntrod = soup.findAll('p', {'class': 'item-intro'})[0]
    except IndexError:
        return -1
    try:
        # posted date
        postedDate = itemIntrod.find_all('span', {'class': 'date'})[0].text
    except IndexError:
        return -1
    try:
        # location
        location = itemIntrod.find_all('span', {'class': 'location'})[0].text
    except IndexError:
        return -1
    try:
        # item price
        price = soup.findAll('span', {'class': 'amount'})[0].text
    except IndexError:
        return -1
    try:
        # item description
        description = soup.findAll('div', {'class': 'item-description'})[0].find_all('p')[0].text
    except IndexError:
        return -1
    try:
        # item properties
        propList = soup.findAll('div', {'class': 'item-properties'})[0]
        arr.append(title);
        arr.append(postedDate)
        arr.append(location)
        arr.append(price)
        arr.append(description)
        keys = propList.find_all('dt')
        values = propList.find_all('dd')
        # if (index == 0):
        #     headers.append('title')
        #     headers.append('posted date')
        #     headers.append('location')
        #     headers.append('price')
        #     headers.append('description')
        #     for index in range(len(keys)):
        #         headers.append(keys[index].text)
        #         arr.append(values[index].text)
        #     return arr, headers
        for index in range(len(keys)):
            # headers.append(keys[index].text)
            arr.append(values[index].text)
    except IndexError:
        return -1
    return arr

# pageCount = 150;
#
# index = 1;
# urls = []
# while(index <= pageCount):
#     url = getUrl(index)
#     res = r.get(url)
#     temp = extractUrls(res.content)
#     if (pageCount != 150 and temp.__len__() < 27):
#         continue
#     print(temp.__len__())
#     urls = urls  + temp
#     # print(url)
#     # print('\n\n\n')
#     # print(urls)
#     # print('\n\n\n')
#     if (urls.__len__() == 0):
#         print('Retry :' + url)
#         continue;
#     index = index + 1;
#     print('Page: ' , index)
#
# with open("urls.txt", "a") as myfile:
#     for url in urls:
#         myfile.write(url + '\n')
# df = pd.DataFrame(urls)
# df.to_csv('urls.csv')
# print(urls)

df = pd.read_csv('urls.csv')
li = []
for index, row in df.iterrows():
    count =0
    while(True):
        res = r.get(row[1])
        rtn = extractItem(res.content)
        print(rtn)
        if (count > 6):
            break;
        if (rtn == -1):
            count = count + 1
            continue
        else:
            li.append(rtn)
            break
df = pd.DataFrame(li)
df.to_csv('houses.csv')
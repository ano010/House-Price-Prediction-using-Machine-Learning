import requests as r
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
from time import sleep
from url import *


url = 'https://ikman.lk/en/ads/sri-lanka/property'
#
# import urllib3
# http = urllib3.PoolManager()
# r = http.request('GET', 'https://ikman.lk/en/ads?page=2')

# print("working")
# response_property_all = r.get(url)

# soup = bs(response_property_all.content)

# allProperties = soup.findAll('div' , { 'class': 'ui-item'})
root = r'./NEW_NEW  _DATA'
def writeHtmlData(dirPath, fileName, htmlString):
    try:
        os.mkdir(dirPath)
        print("Directory " , dirPath ,  " Created ") 
    except FileExistsError:
        # print()
        ''
    file = open(dirPath + r"/" + fileName + '.html', 'wb')
    file.write(htmlString)
    file.close()

def toDirPath(array):
    filePath = None
    for index in range(len(array)):
       
        if (index == 0) :
            filePath = array[index]
            try:
                os.mkdir(array[index])
            except: 
                # print()
                ''
        else :
            filePath += '/' + array[index]
            try :
                os.mkdir(filePath)
            except: 
                # print()
                ''
        
    return filePath;

# print(toDirPath([root, 'colombo', 'kotter']))

# writeHtmlData(toDirPath([root, 'colombo', 'kotter']), 'nf', 'hslfj')
# # dirName = r'F:\Data-set\new'
 
# import os 
# try:
#     # Create target Directory
#     os.mkdir('F:\Data-set\colombo\kotter')
#     print("Directory " , dirName ,  " Created ") 
# except FileExistsError:
#     print("Directory " , dirName ,  " already exists")

# f = open(dirName + '\\new.html', 'w+');
# f.write('hfsf')

def isDuplicatePage(data, page):
    soup = bs(data)
    currentPageElem = soup.findAll('span', {'class': 'is-current'}, text=True)
    print(currentPageElem)
    if (currentPageElem.__len__() == 0):
        return -1
    try:
        pageDom = currentPageElem[0].text
    except IndexError:
        return -1
    if (page == int(pageDom)):
        return 0
    else:
        return 1


def sendRequest(url):
    res = r.get(url, params={'page': page, 'type': 'for_rent'})
    return res.content;

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

def extractItem(content, index):
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
        if (index == 0):
            headers.append('title')
            headers.append('posted date')
            headers.append('location')
            headers.append('price')
            headers.append('description')
            for index in range(len(keys)):
                headers.append(keys[index].text)
                arr.append(values[index].text)
            return arr, headers
        for index in range(len(keys)):
            # headers.append(keys[index].text)
            arr.append(values[index].text)
    except IndexError:
        return -1
    return arr

def fetchItemsRequest(urls, dir):
    data = []
    index = 0
    retryCount = 0;
    while(index < len(urls)):
        res = r.get(urls[index]);
        if res is None:
           print("Retry Item")
           retryCount = retryCount + 1
           if (retryCount >= 10):
               index = index + 1
               retryCount = 0;
               continue
           if(retryCount >= 5):
               
               continue
        # writeHtmlData(dir, str(index), res.content)
        rtn = extractItem(res.content, index)
        if (rtn == -1):
            print("Retry Item")
            retryCount = retryCount + 1
            if (retryCount >= 10):
                index = index + 1
                retryCount = 0;
                continue
            if (retryCount >= 5):
                
                continue
        print(str(index) + ' of   ' + str(len(urls)))

        if (index == 0):
            try:
                data.append(rtn[1])
                data.append(rtn[0])
            except TypeError:
                print("ignored")
        data.append(rtn)
        index = index + 1
    # for index in range(len(urls)):
    #     res = r.get(urls[index]);
    #     if res is None:
    #         continue
    #     writeHtmlData(dir, str(index), res.content)
    #     rtn = extractItem(res.content, index)
    #     print(str(index) +  ':   '+ str(rtn))
    #     if (index == 0):
    #         data.append(rtn[1])
    #         data.append(rtn[0])
    #     data.append(rtn)
    try:
        df = pd.DataFrame(data)
        df.to_csv(dir + r"/" + 'file' + '.csv')
        print("success csv" + " " + dir)
    except TypeError:
        return;


firstTime = True;
for index in range(len(propertyTypes)):
    type = propertyTypes[index]
    print(type);
    # var = input("step over ? [y|n]")
    # if (var == 'y') :
    #

    # if (type != 'new-developments'):
    #     rentFileUrls = getFileInfo(root, type, 'rent')
    #     for key, value in rentFileUrls.items():
    #         # print(str(key)  + '  :  ' +  str(value));
    #         # var = input("step over ? [y|n]\n")
    #         #
    #         # if (var == 'y'):
    #         #     continue
    #         url = getUrl(type, key);
    #         print(url)
    #         if (url == 'https://ikman.lk/en/ads/colombo/new-developments'):
    #             firstTime = False
    #         if (firstTime):
    #             continue
    #         urls = []
    #         res = None
    #         page = 1;
    #         retryCount = 0;
    #         while 1:
    #             try:
    #                 print("comes")
    #                 res = r.get(url, params={'page': page, 'type': 'for_rent'})
    #             except ConnectionError:
    #                 continue
    #             if res is None:
    #                 print(page , ' : ', 'rent : ', 'Failed', url )
    #                 break;
    #
    #             val = isDuplicatePage(res.content, page)
    #             if (val == 0 ) :
    #                 retry = False
    #                 list = extractUrls(res.content)
    #                 if (list != None):
    #                     urls = urls + list
    #                 print(page, ' : ', 'rent : ', 'Success', url)
    #                 # writeHtmlData(toDirPath(value), str(page), res.content)
    #                 page = page + 1
    #             elif (val == -1):
    #               print('Retry page: ' + str(page))
    #               retryCount = retryCount + 1
    #               if (retryCount >= 10):
    #                   retryCount = 0
    #                   page = page + 1
    #                   continue
    #               if (retryCount >= 5):
    #
    #                   continue
    #
    #               # res = r.get(url, params={'page': page, 'type': 'for_rent'})
    #               # if res is None:
    #               #     print(page, ' : ', 'rent : ', 'Failed', url)
    #               #     break;
    #             else:
    #                 break;
    #         fetchItemsRequest(urls, toDirPath(value))



    # if (type != 'holiday-short-term-rental'):
    saleFileUrls = getFileInfo(root, type, 'sale',)
    for key, value in saleFileUrls.items():
        url = getUrl(type, key);
        # url = 'https://ikman.lk/en/ads/wennappuwa/houses';
        print(url, value);
        if (url == 'https://ikman.lk/en/ads/nugegoda/houses'):
            firstTime = False
            # continue;
        if (firstTime):
            continue
        res = None
        page = 1;
        urls = []
        retryCount = 0
        while 1:
            res = r.get(url,params={'page': page, 'type': 'for_sale'})
            if res is None:
                print(page , ' : ', 'sale : ', 'Failed', url )
                break;
            val = isDuplicatePage(res.content, page)
            print(val)
            if (val == 0):
                list = extractUrls(res.content)
                if (list != None):
                    urls = urls + list
                print(page, ' : ', 'sale : ', 'Success', url)
                # writeHtmlData(toDirPath(value), str(page), res.content)

                page = page + 1
            elif (val == -1):
                print('Retry page: ' + str(page))
                retryCount = retryCount + 1
                if (retryCount >= 10):
                    retryCount = 0
                    page = page + 1
                    continue
                if (retryCount >= 5):
                    continue
            else:
                break;

        fetchItemsRequest(urls, toDirPath(value))

    



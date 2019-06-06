import requests as r
from bs4 import BeautifulSoup as bs
import os
from url import *

url = 'https://ikman.lk/en/ads/sri-lanka/property'

response_property_all = r.get(url)
# soup = bs(response_property_all.content)

# allProperties = soup.findAll('div' , { 'class': 'ui-item'})
root = r'F:\Data-set'
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


for index in range(len(propertyTypes)):
    type = propertyTypes[index]
    if (type != 'new-developments'):
        rentFileUrls = getFileInfo(root, type, 'rent')
        for key, value in rentFileUrls.items():
            url = getUrl(type, key);
            # print(url, value);
            res = None
            page = 1;
            while 1: 
                res = r.get(url,params={'page': page, 'type': 'for_rent'})
                if res is None:
                    print(page , ' : ', 'rent : ', 'Failed', url )
                    break; 
                print(page , ' : ', 'rent : ', 'Success', url )
                writeHtmlData(toDirPath(value), str(page), res.content)
                page = page + 1
    if (type != 'holiday-short-term-rental'):
        saleFileUrls = getFileInfo(root, type, 'sale',)
        for key, value in rentFileUrls.items():
            url = getUrl(type, key);
            # print(url, value);
            res = None
            page = 1;
            while 1: 
                res = r.get(url,params={'page': page, 'type': 'sale'})
                if res is None:
                    print(page , ' : ', 'sale : ', 'Failed', url )
                    break; 
                print(page , ' : ', 'sale : ', 'Success', url )
                writeHtmlData(value, str(page), res.content)
                page = page + 1

     

    



from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import nltk
porter = PorterStemmer()
stop_words = set(stopwords.words('english'))
# import inflect
# inflect = inflect.engine()
# nltk.download()


def add_word(word, list):
    #freq_list = []
    for i in range(len(list)):
        if (list[i][0] == word):
            count = list[i][1] + 1
            list[i][1] = count

            return
    list.append([word, 1])


def tokenize_text(str):
    #    print(type(str))
    tokens = word_tokenize(str)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove all tokens that are not alphabetic
    words = [word for word in tokens if word.isalpha()]
    # remove stop words english
    words = [w for w in words if not w in stop_words]
    # stemm
    return words


def isEnglish(str):
    for c in str:
        try:
            c.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
    return True


dfBattramulla = pd.read_csv(
    '../resource/new.csv', encoding='utf-8')

freq_list = []

for index, row in dfBattramulla.iterrows():
    #listTit = tokenize_text(row[1])
    listDesc = tokenize_text(row[5])
    # print(listDesc)
    #lst = listTit + listDesc
    lst = listDesc
    # remove non english char words
    lst = [w for w in lst if isEnglish(w)]
    #lst = list(set(lst))
    # print(lst)
    for w in lst:
        add_word(w, freq_list)

newList = []
while(freq_list):
    max = 1
    for li in freq_list:
        #print(li[0], '    ', li[1])
        if li[1] >= max:
            max = li[1]
            temp = li
    freq_list.remove(temp)
    newList.append(temp)

for li in newList:
    print(li)

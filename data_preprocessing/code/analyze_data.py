import pandas as pd
import bag_of_words as bow
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import bag_of_words as bow
import sys


def find_similar_words(path, word):
    df = pd.read_csv(path, encoding = 'utf-8')

    word_list = []
    for index, row in df.iterrows():

        tit_list = word_tokenize(row[1])
        des_list = word_tokenize(row[5])
        lst = list(set(tit_list + des_list))

        for w in lst:
            word_list.append(w)

    word_list = list(set(word_list))
    word_list = [w.lower() for w in word_list]
    match_indexes = [index for (index, w) in enumerate(word_list) if w.find(word) != -1]

    for i in match_indexes:
        print(word_list[i])

def word_frequency_count(path, *args):
    word_list = bow.create_word_list(path)
    word_list = bow.sort_word_list(word_list)

    if not args:
        count = 0
        for li in word_list:
            count = count + 1
            print(li)
        print('Total: ', count)
    else:
        word = ''
        for li in word_list:
            if li[0].__eq__(args[0]):
                print(li)
                word = li
        if not word:
            print('word dose not exist')

def find_near_words(word, wordList):
    matchIndexes = [index for (index, w)  in enumerate(wordList) if w.find(word) != -1]

    for i in matchIndexes:
        if i == 0:
            return [wordList[i], wordList[i+1], wordList[i+2], wordList[i+3]]
        elif i == wordList.__len__() - 1:
            return [wordList[i-3], wordList[i-2], wordList[i-1], wordList[i]]
        elif i == 1:
            return [wordList[i-1], wordList[i], wordList[i+1], wordList[i+2]]
        elif i == wordList.__len__() - 2:
            return [wordList[i-2], wordList[i-1], wordList[i], wordList[i+1]]
        else:
            return [wordList[i-2], wordList[i-1], wordList[i], wordList[i+1], wordList[i+2]]

def analyze_csv_for_near_words(path, word):
    df = pd.read_csv(path, encoding='utf-8')

    for index, row in df.iterrows():
        str = row[1] + ' ' + row[5]
        stop_words = set(stopwords.words('english'))

        wordList = word_tokenize(str)
        wordList = [w.lower() for w in wordList]
        wordList = [w for w in wordList if not w in stop_words]

        near_words = find_near_words(word, wordList)

        if not near_words:
            continue

        print(near_words)

def is_near(near_word, word, wordList):
    near_words = find_near_words(word, wordList)

    if not near_words:
        return 0

    for w in near_words:
        if w.find(near_word) != -1:
            flag = 1
            break
        else:
            flag = -1

    return flag      

def is_together(path, near_word, word):
    df = pd.read_csv(path, encoding='utf-8')
    flag = True
    for index, row in df.iterrows():
        str = row[1] + ' ' + row[5]
        stop_words = set(stopwords.words('english'))

        wordList = word_tokenize(str)
        wordList = [w.lower() for w in wordList]
        wordList = [w for w in wordList if not w in stop_words]

        near_words = find_near_words(word, wordList)
        
        if is_near(near_word, word, wordList) == 0:
            continue    

        if is_near(near_word, word, wordList) == -1:
            print(near_words)
            print(row[0], ' : ' + row[1] + ' :False')
            flag = False
        else:
            print(near_words)
            print(row[0], ' : ' + row[1] + ' :True')
    return flag       


if sys.argv[1].__eq__('-fre') and len(sys.argv) != 3:
    word_frequency_count('../resource/new.csv')
elif sys.argv[1].__eq__('-fre') and len(sys.argv) == 3:
    word_frequency_count('../resource/new.csv', sys.argv[2])
elif sys.argv[1].__eq__('-sim'):
    find_similar_words('../resource/new.csv', sys.argv[2])
elif sys.argv[1].__eq__('-near'):
    analyze_csv_for_near_words('../resource/new.csv', sys.argv[2])
elif sys.argv[1].__eq__('-tog') and sys.argv[2] and sys.argv[3]:
    print(is_together('../resource/new.csv', sys.argv[2], sys.argv[3]))

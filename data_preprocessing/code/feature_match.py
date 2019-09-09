import pandas as pd
import nltk;
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
import sys

def check_word(word, list):
    match_indexes = [index for (index, w) in enumerate(word_list) if w.find(word) != -1]

    if match_indexes:
        return True
    else:
        return False

#print(check_word('bra', word_list))

def tokenize_text(str):
    # print(type(str))
   tokens = word_tokenize(str)
   # convert to lower case
   tokens = [w.lower() for w in tokens]
   return tokens

def compare_str(tokens, word):
    i = -23
    try:
        i = tokens.index(word)
    except ValueError:
        try:
            i = [index for (index, w)  in enumerate(tokens) if w.find(word) != -1][0]
        
        except IndexError:
            pass
    return i

df = pd.read_csv('new.csv', encoding = 'utf-8')

for index, row in df.iterrows():
    tit_list = tokenize_text(row[1])
    des_list = tokenize_text(row[5])
    word_list = tit_list + des_list
    word_list = list(set(word_list))

    if check_word('old', word_list):
        print(row[1] + ': ' + row[5] + '\n')

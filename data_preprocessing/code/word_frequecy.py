from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import nltk
porter = PorterStemmer()
stop_words = set(stopwords.words('english'))

# nltk.download()


def isEnglish(str):
    for c in str:
        try:
            c.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
    return True


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


def analyse_csv(path, *colums):
    df = pd.read_csv(path)
    l_of_title_desc = [row[1] + '  ' + row[7]
                       for (index, row) in df.iterrows()]
    
    words = [w for text in l_of_title_desc for w in tokenize_text(
        text) if isEnglish(w)]
    print(len(words))
    unique_words = list(set(words))
    words_freq = [(w, words.count(w)) for w in unique_words]
    words_freq.sort(key=lambda x: x[1])
    for t in words_freq:
        print(t[0], '  :   ', t[1])


analyse_csv('houses_original.csv', '')

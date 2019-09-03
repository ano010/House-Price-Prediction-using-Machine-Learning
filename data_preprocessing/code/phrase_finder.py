import pandas as pd
import nltk;
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
import sys

def tokenize_text(str):
    #    print(type(str))
   tokens = word_tokenize(str)
   # convert to lower case
   tokens = [w.lower() for w in tokens]
   return tokens

def compare_str(tokens, word):
    i = -23;
    try:
        i = tokens.index(word);
    except ValueError:
        try:
            i = [index for (index, w)  in enumerate(tokens) if w.find(word) != -1][0]
        except IndexError:
            pass
    return i;
def analyse_word(path, word=''):
    df = pd.read_csv(path)
    print()
    l_of_title_desc = [ (row[0], tokenize_text(row[1] + '  ' + row[5])) for (index, row) in df.iterrows() if index != 0];
    # l_of_title_desc = [list(set(title_desc))    for title_desc in l_of_title_desc];
    phrases = []
    for (key ,ti_des) in l_of_title_desc:
        try:
            i = compare_str(ti_des, word);
            phrase = ''
            if i == -23:
                phrases.append((key, '          empty          '))
                continue
            elif (i == 0):
                phrase = ti_des[i] + '  ' + ti_des[i+1]
            else:
                phrase = ti_des[i-1] + '    ' + ti_des[i] + '  ' + ti_des[i+1]
            phrases.append((key, phrase ))
        except IndexError:
            pass
    
    for phrase in phrases:
        print(phrase[0], '    :   ' , phrase[1]) 

    print()
    print('Number of houses: ', len(phrases))




analyse_word('../resource/new.csv', sys.argv[1])
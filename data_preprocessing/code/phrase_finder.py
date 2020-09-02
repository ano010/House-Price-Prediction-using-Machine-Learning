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
    l_of_title_desc = [ (row[0], tokenize_text(row[1] + '  ' + row[5])) for (index, row) in df.iterrows() if row[0] != 'ID'];
    # l_of_title_desc = [list(set(title_desc))    for title_desc in l_of_title_desc];
    phrases = []
    for (key ,ti_des) in l_of_title_desc:
        try:
            i = compare_str(ti_des, word);
            phrase = ''
            if i == -23:
                phrases.append((key, '1'))
                continue
            else:
                phrase = ti_des[i-1] + '  ' + ti_des[i]
            # elif (i == 0):
            #     phrase = ti_des[i] + '  ' + ti_des[i+1]
            # else:
            #     phrase = ti_des[i-1] + '    ' + ti_des[i] + '  ' + ti_des[i+1]
            phrases.append((key, phrase ))
        except IndexError:
            phrases.append((key, ti_des[i]))
            pass
    
    # for phrase in phrases:
    #     print(phrase[0], '    :   ' , phrase[1]) 

    print()
    print('Number of houses: ', len(phrases))
    return phrases



related_words = {
    'storey': ['storied', 'storyed', 'story',
                'storey', 'stories', 'storeid', 'storie'],
    'one': ['single', 'one','1', 'singal', 'sigle'],
    'two': ['two', '2', 'tow', 'double'],
    'three': ['three', '3'],
    'four': ['four', '4']
}

def isContains(text, l):
    for w in l:
        if text.find(w) != -1:
            return True
    return False 



phrases = analyse_word('../resource/new.csv', sys.argv[1])
# for (key, i) in phrases:
#     print(key, '   :   ', i)
li = []
for (key, w) in phrases:
    if isContains(w, related_words['storey']):
        if w == '1': 
            li.append([key, 1])
        elif isContains(w, related_words['one']):
            li.append([key, 1])
        elif isContains(w, related_words['two']):
            li.append([key, 2])
        elif isContains(w, related_words['three']):
            li.append([key, 3])
        elif isContains(w, related_words['four']):
            li.append([key, 4])
        else:
            li.append([key, -1])
    else:
        li.append([key, 1])
# print(li)
df = pd.DataFrame(li) 
df.to_csv('../resource/storey.csv', index=False);  



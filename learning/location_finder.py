import pandas as pd
import nltk;
import inflect
inflect = inflect.engine()
# nltk.download()
words = set(nltk.corpus.words.words())
pStemmer = nltk.PorterStemmer()
sStemmer = nltk.SnowballStemmer('english')


locFreqDict = {}

def find_locations(str):
    for w in nltk.wordpunct_tokenize(str):
        # w = sStemmer.stem(w)
        if not(w.lower() in words) and  w.isalpha() and not(w.endswith('s')):
            w = w.lower()
            try:
                freq = locFreqDict[w];
                locFreqDict[w] = freq + 1;
            except KeyError:
                locFreqDict[w] = 1;

# find_locations('200m to main pelawatta junction 20ft rd facing superb land with an old house 13.5.perches land square land high land natural soil. Highly residential area 500m to parliament very close to battaramulla Colombo Rajagiriya all government departments and offices are very close price 3500000.per perch genuine buyers well come appointments')
dfBattramulla = pd.read_csv('/home/shank/Desktop/ml-real-estate/Machine-Learning-in-real-estate-industry/learning/data-for-extraction/land/sale/colombo/battaramulla/file.csv', encoding='utf-8')

for index, row in dfBattramulla.iterrows():
    find_locations(row[1])
# print(locFreqDict.items())
for key in locFreqDict:
    print(key + ' : ' + str(locFreqDict[key]));
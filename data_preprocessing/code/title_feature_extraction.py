import bag_of_words
import pandas as pd

df = pd.read_csv('../resource/new.csv', encoding='utf-8')

build_identifiers = ['new', 'newly', 'bnew', 'brandnew', 'b']
df['Build'] = ''
for index, row in df.iterrows():
    listTit = bag_of_words.tokenize_text(row[1])
    listTit = [w for w in listTit if bag_of_words.isEnglish(w)]
    listTit = list(set(listTit))
    if any(identifier in listTit for identifier in build_identifiers):
        df.set_value(index, 'Build', 2)
    elif 'old' in listTit:
        df.set_value(index, 'Build', 0)
    else:
        df.set_value(index, 'Build', 1)

print(df)
df.to_csv('houses_with_build_feature.csv', index=False)

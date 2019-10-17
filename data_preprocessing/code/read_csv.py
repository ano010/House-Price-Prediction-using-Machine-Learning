import pandas as pd
import csv


df = pd.read_csv('../resource/data_set_535_ano_sankee.csv')

for index, row in df.iterrows():
    if not isinstance(row[0], float):
        print(row[0])

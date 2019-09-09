import pandas
import csv

df = pandas.read_csv('houses_original.csv')

print(df)

my_list = []

for index, row in df.iterrows():
    if((row[6]) and (row[6].isnumeric())):
        beds = row[6]
        baths = row[7]
        house_size = row[8]
        land_size = row[9]
        row[6] = ''
        row[7] = beds
        row[8] = baths
        row[9] = house_size
        row[10] = land_size
    my_list.append(row)
my_dataframe = pandas.DataFrame(my_list)
my_dataframe.to_csv('new.csv', index=False)
import pandas
import csv


df = pandas.read_csv('houses.csv')

print(df)

my_list = []

for index, row in df.iterrows():
    if(row[6].isnumeric()):
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

# row = [['2', ' Marie', ' California'], ['3', ' Marief',
#                                         ' Californiaf'], ['3', ' Marief', ' Californiaf']]

# with open('new.csv', 'w', newline='') as writeFile:
#     writer = csv.writer(writeFile, delimiter=',')
#     print(my_list[0])
#     writer.writerows(my_list)

# writeFile.close()

# for element in my_list:
#     print(element[9])

import csv
row = [['2', ' Marie', ' California'], ['3', ' Marief',
                                        ' Californiaf'], ['3', ' Marief', ' Californiaf']]

lines = row
with open('new.csv', 'w', newline='') as writeFile:
    writer = csv.writer(writeFile, delimiter=',', )
    writer.writerows(row)

writeFile.close()

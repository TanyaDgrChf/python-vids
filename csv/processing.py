import csv

with open('output_gdp_2022.csv', 'r', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    print(header)
    for row in csv_reader:
        if row[1] == '':
            row[1] = 0
        else:
            row[1] = int(float(row[1]))
        if row[1] < 5000 and row[1] != 0:
            print(row)

    
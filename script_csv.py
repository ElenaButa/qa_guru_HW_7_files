import csv
from pandas import *


with open('resources/eggs.csv', 'w') as csvfile:
    csfile = csv.writer(csvfile, delimiter=',')
    csfile.writerow(['Jane', 'Jade'])
    csfile.writerow(['John', 'Jhoan'])
with open("resources/eggs.csv", 'r') as csvfile:
    num_lines = sum(0 for row in csvfile)
    print(num_lines)

    num_column = sum(1 for column in csvfile)
    print(num_column)
#assert num_column == 0

with open('resources/username.csv', 'r') as csvfile:
     csvfile = csv.reader(csvfile)

rows = []
    with open("resources/eggs.csv") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) > 0:
                rows.append(row)
print(len(row))
    #assert len(row) in rows
    #assert line_with_name_2 in rows
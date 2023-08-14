import csv
# TODO оформить в тест, добавить ассерты и использовать универсальный путь
import os.path

path1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources/username.csv')

def test_check():
    with open(path1, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])
    with open(path1, 'r') as csvfile:
        num_lines = sum(1 for line in csvfile)
        print(num_lines)
        assert num_lines == 4


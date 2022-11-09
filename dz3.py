import argparse

parser = argparse.ArgumentParser()

parser.add_argument('path', type = str, help = 'Путь к файлу')
parser.add_argument('word', help = "Искомое слово")

args = parser.parse_args()

with open(args.path, 'r', encoding = 'utf-8') as f:
    d = open("строки.log", 'r+', encoding = 'utf-8')
    for line in f:
        l = f.readline()
        if args.word in l:
            d.write(l)
            print(l)
    d.close

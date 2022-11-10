import argparse
import os

parser = argparse.ArgumentParser()

#дз222.py Folder C:\Users\Sallarion\Desktop\проверка error
parser.add_argument('path', type = str, help = "The path to the file or folder")
parser.add_argument('word', help = "The search wold")

args = parser.parse_args()

path = os.path.isfile(args.path)

def word_search():
    with open("list.log", 'a+', encoding = 'utf-8') as d:
            d.write("Result from " + w + ":\n" )
            with open(w, 'r', encoding = 'utf-8') as f:            
                for line in f:
                    if args.word in line:
                        print(line.strip())
                        d.write(line)
    
if path == True:
    w = args.path
    word_search()
    
else:    
    files = os.listdir(args.path)
    for filename in files:
        w = os.path.join(args.path, filename)
        print(w) 
        word_search()
                       

           
                            

         

import argparse
import os
from tqdm import tqdm
import time

parser = argparse.ArgumentParser()

#дз222.py C:\Users\Sallarion\Desktop\проверка error
parser.add_argument('path', type = str, help = "The path to the file or folder")
parser.add_argument('word', help = "The search wold")

args = parser.parse_args()

path = os.path.isfile(args.path)

def word_search():
    total_lines = 0
    search_strings = 0
    with open("list.log", 'a+', encoding = 'utf-8') as d:
            d.write("Result from " + w + ":\n" )
            with open(w, 'r', encoding = 'utf-8') as f:            
                for line in f:
                    total_lines = total_lines + 1
                    if args.word in line:
                        search_strings = search_strings + 1
                        d.write(line)
                        
    for i in tqdm(range(total_lines), desc = "File reading progress"):
        time.sleep(0.0001)
        
    print("Row count: " + str(search_strings))                

if path == True:
    w = args.path
    word_search()
    
else:    
    files = os.listdir(args.path)
    for filename in files:
        w = os.path.join(args.path, filename)
        print(w) 
        word_search()
                       

           
                            

         

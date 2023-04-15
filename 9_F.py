import os
os.system('cls')

with open("9_F.txt",'r') as reader:
    # for line in list(reader):
    for line in reader:
        print(line,end='')
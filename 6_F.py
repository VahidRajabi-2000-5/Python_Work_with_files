import os
os.system('cls')

names = ['vahid', 'yasin', 'yasamin', 'mohammad taha']
with open('6_F.txt', 'w') as f:
    # f.writelines(map(lambda name:name+'\n',names))
    f.writelines('\n'.join(names))

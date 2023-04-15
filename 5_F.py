import os
os.system('cls')

names = []
#خودش فایل رو باز میکنه و باز نگه میداره تا کار ما تموم بشه بعد خودش خودکار میبنده with
#نیست try except  دیگه نیاز به  

with open('5_F.txt','r') as list_of_family_names:
    for name in list_of_family_names.read().split('\n'):
        names.append(name)
    
print(names)
print("END")
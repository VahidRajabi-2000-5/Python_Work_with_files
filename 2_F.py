import os
os.system('cls')

f = open('2_F.txt', 'r')

result = f.read()
print(type(result))
print(result.split())
print()
for name in result.split():
    print(name+'s')

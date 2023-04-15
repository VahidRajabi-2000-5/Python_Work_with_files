import os
os.system('cls')

f = open("4_F.txt", 'r')
try:
        
    # در این خط استرینگ ذخیره میشه
    resault = f.read()
    resault = resault.split("\n")

    print(resault)
    while True:
        username = input("Enter your name: ")
        if username == "exit":
            break
        resault.append(username)
        print(resault)
finally:
    f.close()
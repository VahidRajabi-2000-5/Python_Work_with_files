import os
os.system('cls')

f = open('3_F.txt', 'r')

# '\n' اسامی رو به صورت لیست تحویل میده به همراه
resault = f.readlines()
print(resault)
# ===========================

while True:
    line = f.readline()
    print(line, end="")
    if line == '':
        break
# خروجی
# ['vahid\n', 'yasin\n', 'yasamin\n', 'mohammad taha\n', 'rahim\n', 'roghaye']
# اگر الان کد رو ران کنیم دیگه حلقه پایینی اجرا نمیشه چون خود پایتون یک اشارگر داره
#'e' حالا یک دوره فایل رو خونده رسیده به آخر اسم رقیه 
# دیگه در ادامه چیزی نیست و دیگه نمی تونه بره جلو
# در حلقه میگیم دوباره بخون چون در ادامه هیچی نیست دیگه حلقه چیزی نمایش نمیده
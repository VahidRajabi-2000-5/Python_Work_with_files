import os
os.system('cls')

file_name = input("Enter your file name: ")

# یک فایل رو باز کن
# اول اسم فایل رو میدی دوم میگی که بنوسه یا بخونه
# "w" write  "r" read اگر بخوای بنویسی هر سری اطلاعات داخل فایل رو پاک و دوباره نویسی میکنه به واسطه این کلید واژه ها
# اگر فایل وجود داشت و داخلش مقادیر بود و دوباره با همون نام فایل ساختیم دوباره نویسی میشه ومقادیر پاک میشه
f = open(f"{file_name}.txt", "w")


# نوشتن داخل فایل
f.write("Hello.How are you?\n")
f.write("Hello.How are you?")
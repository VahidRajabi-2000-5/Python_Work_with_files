import os
os.system('cls')


print('--- current grades ---')
with open('8_F.txt', 'r') as reader:
    all_data = reader.read()
    print(all_data.split('\n'))

yes_no_new_grades = input("Do you want to add new grades? ")

new_grades = []
if yes_no_new_grades == "y":
    while True:
        name = input('Enter Name: ')

        if name == 'exit':
            break

        grade = input('Enter grade: ')
        new_grades.append({
            'name': name,
            'grade': int(grade),
        })

with open('8_F.txt','a') as grades_file:
    for student_grade in new_grades:
        grades_file.write(f'\n{student_grade["name"]} {student_grade["grade"]}')
        
        
# گرفتن نمرات 
all_students_grades=[]
with open('8_F.txt','r') as reader:
    all_data = reader.read()
    for line in all_data.split('\n'):
        x = line.split(' ')
        grade = x[1]
        all_students_grades.append(int(grade))
        

print(sum(all_students_grades)/len(all_students_grades))
import os
import json
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
 
known_friends = set(input("Enter you friend's names separated by ',': ").split(','))
my_file = os.path.join(THIS_FOLDER, 'names.txt')
my_file_data = open(my_file, 'r')
names_list = my_file_data.readlines()
my_file_data.close()

formated_names = set([name.strip() for name in names_list])
print(formated_names)

friends_near =known_friends.intersection(formated_names)
print(friends_near)

friends_near_file = open(os.path.join(THIS_FOLDER,"friend_names.txt"),'w')
for friend in friends_near:
    friends_near_file.write(f'{friend}\n')

friends_near_file.close()

question_file = open(os.path.join(THIS_FOLDER,'questions.txt'),'r')
question_data = question_file.readlines()
question_file.close()
formated_questions = [question.strip() for question in question_data]
current_score=0
print(formated_questions)
for question in formated_questions:
    print(question)
    curr_question = question.split('=')
    answer = input(f'{curr_question[0]} equals to: ')
    if answer == curr_question[1]:
        current_score+=1

final_score=f'{current_score}/{len(question_data)}'
output_file = open(os.path.join(THIS_FOLDER,'result.txt'),'w')
output_file.write(final_score)
output_file.close()


file = open(os.path.join(THIS_FOLDER,'csv_data.csv'),'r')
file_data = file.readlines()
file.close()
file_data = [line.strip() for line in file_data[1:]]

for line in file_data:
    student = line.split(',')
    name,age,university,degree = student
    print(f'{name} is {age}, studying {degree} at {university}')

json_file = open(os.path.join(THIS_FOLDER,'students_json.json'),'r')
json_content = json.load(json_file)
json_file.close()
print(json_content)

cars = [
    {"make": "Toyota", "model": "Camry"},
    {"make": "Honda", "model": "Accord"},
    {"make": "Ford", "model": "Mustang"},
    {"make": "Chevrolet", "model": "Cruze"},
    {"make": "Tesla", "model": "Model 3"},
]

with open(os.path.join(THIS_FOLDER,'cars_json.json'), 'w', encoding='utf-8') as f:
    json.dump(cars, f, ensure_ascii=False, indent=4)
    

import file_operations
file_operations.save_to_file('test','data.txt')

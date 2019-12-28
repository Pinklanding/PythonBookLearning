with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())

file_path = '/Users/guanchun/PycharmProjects/191219/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())

file_path = '/Users/guanchun/PycharmProjects/191219/pi_digits.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

file_path = '/Users/guanchun/PycharmProjects/191219/pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

if str(23) in pi_string:
    print('yes')

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I like coding.\n')

with open(filename, 'a') as file_object:
    file_object.write('We like coding\n')

try:
    print(5/0)
except ZeroDivisionError:
    print("!!! Cannot divide by zero")

filename = 'a.txt'
try:
    with open(filename, 'r') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print('No such file')

title = 'sadf eer sss gghrh'
print(title.split())

filename = 'a.txt'
try:
    with open(filename, 'r') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    pass

#### json

import json

number = [1,4,2,4,6,3,5,22,45]
filename = 'number.json'
with open(filename, 'w') as file_o:
    json.dump(number,file_o)

with open(filename) as file_o:
    new_number = json.load(file_o)
print(new_number)

import json

filename = 'username2.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("name")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("hello " + username)
else:
    print("hi " + username)


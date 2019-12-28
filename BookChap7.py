msg = "Hello, please input your first name.\n"
msg += "Input:"
name = input(msg)
print("Your name is " + name.title())

msg2 = "How old are you?"
age = int(input(msg2))
if age >= 18:
    print("Adult")
else:
    print("Not adult")

print(4%3)
print(7/2)
print(7%2)
print(8%4)

def even_or_odd():
    number = int(input("Please input an integer:"))
    if number%2 == 0:
        print("even")
    else:
        print("odd")

even_or_odd()


c_number = 1
while c_number <= 5:
    print(c_number)
    c_number +=1

msg = "Type in anything:\n"
msg += "(or type in 'quit' to quit.)"
typein = ''
while typein!='quit':
    typein = input(msg)
    if typein != 'quit':
        print(typein)

msg = "Type in anything:\n"
msg += "(or type in 'quit' to quit.)"
typein = ''
active = True
while active:
    typein = input(msg)

    if typein == 'quit':
        active = False
    else:
        print(typein)

msg = "Type in anything:\n"
msg += "(or type in 'quit' to quit.)"
typein = ''
active = True
while active:
    typein = input(msg)

    if typein == 'quit':
        active = False
        print("JUMP")
    elif typein == "Woo":
        break
        print("JUMP")
    elif typein =="tbc":
        continue
        print("JUMP")
    else:
        print(typein)
        print("JUMP")

print("TBC")

uncfm_users = ['a','b','c','a']
cfmd_users = []

while uncfm_users:
    curr_user = uncfm_users.pop()

    print("Confirming " + curr_user.title() + '...')

    cfmd_users.append(curr_user)

print(uncfm_users)
print(cfmd_users)

while 'a' in cfmd_users:
    cfmd_users.remove('a')

print(cfmd_users)

survey = {}

active = True

while active:
    msg1 = "please input name:"
    msg2 = "please answer question:"

    name = input(msg1)
    answer = input(msg2)

    survey[name]=answer

    tbc = input("Anyone else?")
    if tbc == 'no':
        active = False

print(survey)
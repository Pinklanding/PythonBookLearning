cars = ['audi', 'bMw', 'benz', 'toyota']
for car in cars:
    if car.lower() == 'bmw':
        print(car.upper()+'\n')
    else:
        print(car.title()+'\n')

for car in cars:
    if car.lower() != "bmw":
        print(car.title())
    else:
        print(car.upper())

#answer = input()
def guessNumber(answer):
    guess = int(input())
    while answer != guess:
        if answer < guess:
            print("Smaller")
            guess = int(input())
        else:
            print("Bigger")
            guess = int(input())
    print("Congs!")

#guessNumber(3)

print('audi' in cars)
print('acd' in cars)

age = 12
def agecheck(age):
    if age < 4:
        print(0)
    elif age <= 18:
       print(5)
    elif age <= 65:
       print(10)
    elif age > 65:
        print(1)

agecheck(2)
agecheck(18)
agecheck(26)
agecheck(66)

toppings = []
if toppings:
    for topping in toppings:
        print(topping)
else:
    print("empty")

toppings=['1','2','3','4','5']
request_toppings=['1','3']

for request_topping in request_toppings:
    if request_topping in toppings:
        print("ok")



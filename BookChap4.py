import datetime

magicians = ['alice','david', 'carolina']
for magician in magicians:
    print(magician.title() + ' is a great magician!')
    print('I cannot wait to see your show, ' + magician + '\n')
print('Thanks\n\n')

pizzas = ['marg', 'meat', 'seafood']
for pizza in pizzas:
    print("I love " + pizza + ' pizza!')
print("I love pizza!")

for n in range(1,10):
    print(n)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for number in even_numbers:
    square = number**2
    squares.append(square)
print(squares)

tribsqures = []
for number in even_numbers:
    tribsqures.append(number**3)
print(tribsqures)

stat_n = [min(tribsqures),max(tribsqures),sum(tribsqures)]

print(stat_n)

squares = [value**2 for value in range(1,11)]
print(squares)

def million():
    million_list = list(range(1,1000001))
    check = [min(million_list),max(million_list)]
    print(check)
    time_start = datetime.datetime.now()
    sum(million_list)
    time_end = datetime.datetime.now()
    time_used = time_end-time_start
    print(time_used)

#million()

squares = [value*3 for value in range(int(3/3),int(30/3+1))]
print(squares)

print(squares[-3:])
for number in squares[-5:]:
    print(number)

new_number = squares[-3:]
print(new_number)

new_number = squares
squares.append(1233)
print(new_number)
print(squares)

new_number = squares[:]
squares.append(45523)
print(new_number)
print(squares)

####tuple

dimensions = (200,40)
print(dimensions)

for dimension in dimensions:
    print(dimension)

dimensions = (100,20)
print(dimensions)
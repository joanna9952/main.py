# exercise 1
def name_age():
    name = str(input('Enter your name '))
    age = int(input('Enter your age '))
    print(f'Hello {name}. Your age is: {age}')
    x = f'{name}{age}'
    return print(x)

name_age()

# exercise 2
def swap_integers(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp

    print('After swap:')
    print('x = ', num1)
    print('y = ', num2)
    print()
    z = f'{num1}{num2}'
    return print('Return value:', z)

num1 = int(input('x = '))
num2 = int(input('y = '))
print()

print('x = ', num1)
print('y = ', num2)
print()

swap_integers(num1, num2)

#exercise 3
def check_numbers(num1, num2):
    if (num1 % 6 == 0 or num2 % 6 == 0) and (num1 % 10 == 0 and num2 % 10 == 0):
        return print('True')
    else:
        return print('False')


num1 = int(input('num1 = '))
num2 = int(input('num2 = '))

check_numbers(num1, num2)

#exercise 4:
def sum_up(num1, num2):
    sum = int((num2 * (num2 + 1) / 2) - (num1 * (num1 + 1) / 2) + num1)
    if num2 > num1 and (num1 and num2 > 0):
        return print('sum =', sum)
    else:
        return print ('0')


num1 = int(input('num1 = '))
num2 = int(input('num2 = '))

sum_up(num1, num2)

#exercise 5
def circle_area(r1, r2, r3):
    area1 = 3.14 * (r1*r1)
    area2 = 3.14 * (r2*r2)
    area3 = 3.14 * (r3*r3)
    print(f'area1 = {area1}, area2 = {area2}, area3 = {area3}')
    sum = round(float(area1 + area2 + area3))
    return print('sum =', sum)

r1 = int(input('r1 = '))
r2 = int(input('r2 = '))
r3 = int(input('r3 = '))

circle_area(r1, r2, r3)

# #exercise 6
def check_string(text):
    if text.startswith('A') or text.startswith('a') or text.endswith('a') or text.endswith('A'):
        return print('True')
    else:
        return print('False')


text = str(input('Enter your text: '))

check_string(text)

#exercise 7
def triangle(rows):
    for x in range(0, rows):
        for y in range (0, x + 1):
            print('*', end='')
        print()

rows = int(input('rows = '))

triangle(rows)

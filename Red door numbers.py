"""

This code is an absolute mess because I did this and had it working, but then 
I wanted the output to be a lot cleaner, so I just built on top of a crappy
foundation.  
Basically the first 3 variables can be changed.  times_printed is the desired
number of outputs.  target_number is self explanatory.  numbers_list is the 
list of numbers that you want to do operations on to get to the target number.

Inspiration for this came from wanting to find some mathematical relation
between what-a-burger number tags and we really struggled.

**Note**  It can't handle two identical numbers in numbers_list.  This is because
dictionaries are used heavily and one key can't have multiple mappings.

"""


import random

times_printed = 20
target_number = 100
numbers_list = [3, 9, 23, 27, 28, 40, 48]

def change_total(num1, num2, steps):
    grrr = random.randint(0, 8)
    if grrr >= 6:
        steps.append("multiplied {} by {}".format(num1, num2))
        return num1 * num2
    elif grrr <= 2:
        steps.append("subtracted {} from {}".format(num2, num1))
        return num1 - num2
    else: 
        steps.append("added {} to {}".format(num1, num2))
        return num1 + num2

def decifer_steps(steps, numbers):
    dic = {n: n for n in numbers}
    for step in steps:
        splitted = step.split()
        if splitted[0] == 'subtracted':
            new = int(splitted[3]) - int(splitted[1])
            dic[new] = '({} - {})'.format(dic[int(splitted[3])], dic[int(splitted[1])])
            dic.pop(int(splitted[3]))
            dic.pop(int(splitted[1]))
        if splitted[0] == 'added':
            new = int(splitted[3]) + int(splitted[1])
            dic[new] = '({} + {})'.format(dic[int(splitted[3])], dic[int(splitted[1])])
            dic.pop(int(splitted[3]))
            dic.pop(int(splitted[1]))
        if splitted[0] == 'multiplied':
            new = int(splitted[3]) * int(splitted[1])
            dic[new] = '({} * {})'.format(dic[int(splitted[3])], dic[int(splitted[1])])
            dic.pop(int(splitted[3]))
            dic.pop(int(splitted[1]))
    global target_number
    return dic[target_number]

done = False
prints = 0

while done == False:
    steps = []
    counter = 0
    numbers = numbers_list.copy()
    for i in range(len(numbers_list) - 1):
        number1 = random.choice(numbers)
        number2 = random.choice(numbers)
        while number1 == number2:
            counter += 1
            number2 = random.choice(numbers)
            if counter > 15:
                break
        if counter > 15:
            counter = 0
            break
        numbers.remove(number1)
        numbers.remove(number2)
        numbers.append(change_total(number1, number2, steps))

    if numbers[0] == target_number:
        try:
            print(decifer_steps(steps, numbers_list) + ' = {}\n'.format(target_number))
            prints += 1
            if prints >= times_printed:
                done = True
        except:
            pass
        

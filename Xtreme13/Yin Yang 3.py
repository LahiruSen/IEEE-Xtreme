import random

def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

N  = get_number()
string = ""

for i in range(N):

    if (random.random() * 3) % 2 == 0 and (random.random() * 5) % 2 == 0:
        string += 'Y'
    else:
        string += 'y'

print(string)
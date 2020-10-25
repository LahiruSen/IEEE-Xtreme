import math

# a simple parser for python. use get_number() and get_word() to read
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
def get_list():
    input_list = []
    for i in range(6):
        input_list.append(get_number())
    return input_list

# input = get_list()
input = [8, 5, 3, 2, 100, 3]

W, H, A, B, M, C = input[0], input[1], input[2], input[3], input[4], input[5],

X = W/A
Y = H/B

tilePrice = math.ceil((math.ceil(X)*math.ceil(Y))/10)*M
cuttingPrice = 0
if X % 1 != 0:
    cuttingPrice += ((H//B)*B + (H%B))*C
if Y % 1 != 0:
    cuttingPrice += ((W//A)*A + (W%A))*C

print(tilePrice+ cuttingPrice)

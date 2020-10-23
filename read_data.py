# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)

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
    n = get_number()
    for i in range(n):
        array = list(map(int, input().split()))
        input_list.append(array)
    return input_list

def get_str_list():
    data = []
    while True:
        try:
            x = get_number()

            for i in range(str(x)):
                data.append(input().split())
        except EOFError:
            break
    return data

input_parser = parser()
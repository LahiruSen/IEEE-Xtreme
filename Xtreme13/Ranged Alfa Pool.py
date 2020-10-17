# data = list(input().split(' '))
# x=data[0]
data = []


# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


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


while True:
    try:
        x = get_number()

        for i in range(int(x)):
            data.append(input().split())
    except EOFError:
        break
rowData = {"1": 2, "2": 2, "3": 4, "4": 6, "5": 8}

for i in data:
    ans = 0
    low = int(i[0])
    high = int(i[1])
    if (high > 5):
        ans += (high - 1) * 2
    else:
        for j in range(low, high + 1):
            ans += rowData[str(j)]
    print(ans)

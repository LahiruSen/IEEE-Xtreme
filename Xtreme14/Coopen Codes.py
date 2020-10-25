import itertools

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


def get_list(n):
    input_list = []
    for i in range(n):
        array = list(map(str, input().split()))
        input_list.append(array)
    return input_list


# N = get_number()
# codes = get_list(N)

N = 6
codes = [['WELC-OMET-OTHE'], ['IEEE-XTRE-ME14'], ['AAAA-0000-A0A0'], ['AAAA-0000-A0A1'], ['AAAA-0000-A0AB'], ['AAAA-0000-ABAB']]

# print(N)
# print(codes)


# Function to calculate
# Hamming distance
def hammingDist(str1, str2):
    i = 0
    count = 0
    while (i < len(str1) and count <3):
        if (str1[i] != str2[i]):
            count += 1
        i += 1
    if count == 1:
        return True
    else:return False

ans = 0
for a, b in itertools.combinations(codes, 2):
    if hammingDist(a[0], b[0]):
        ans+= 1

print(ans)

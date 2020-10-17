import random
from itertools import chain


def findDuplicates(ini_dict):
    rev_dict = {}
    for key, value in ini_dict.items():
        rev_dict.setdefault(value, set()).add(key)

    result = set(chain.from_iterable(
        values for key, values in rev_dict.items()
        if len(values) > 1))
    return list(result)


# lines = []
# while True:
#     try:
#         line = input()
#     except EOFError:
#         break
#     lines.append(line)
# N = int(lines[0])

N = int(input())
one = [i + 1 for i in range(2 * N)]
# two = [i+1 for i in range(N,2*N)]
Continue = True
DictVal = {}

while (Continue):
    if (len(one) > 0):
        if (len(DictVal) >= 2):
            list112 = sorted(findDuplicates(DictVal))
            if (len(list112) >= 2):
                c1 = list112[0]
                c2 = list112[1]
                del DictVal[list112[0]]
                del DictVal[list112[1]]
            else:
                c1 = random.choice(one)
            c2 = random.choice(one)
            while (c1 == c2):
                c2 = random.choice(one)
        else:
            c1 = random.choice(one)
            c2 = random.choice(one)
            while (c1 == c2):
                c2 = random.choice(one)

        print(c1, " ", c2, "\r", )
        res = input().split(" ")
        if (len(res) == 0):
            continue
        if (len(res) == 2):
            DictVal[c1] = int(res[0])
            DictVal[c2] = int(res[1])
        elif (res[0] == "-1"):
            break
        elif (res[0] == "MATCH"):
            one.remove(c1)
            one.remove(c2)
        else:
            continue
    else:
        Continue = False
        print(-1)
        break
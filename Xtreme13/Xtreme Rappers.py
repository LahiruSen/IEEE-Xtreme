# data = list(input().split(' '))
# x=data[0]
# y=data[1]

# def calculate(x,y):
#     numOfPhases = 0
#     x = int(x)
#     y= int(y)
#     while(x>0 and y>0 ):
#         if(x==y):
#             if(x==1):
#                 x-=1
#                 y-=1
#                 continue
#             else:
#                 x -=1
#                 y -=2
#                 if(x>=0 or y>=0):
#                     numOfPhases = numOfPhases+1
#                     continue
#         elif(x<y):
#             x-=1
#             y-=2
#             if(x>=0 or y>=0):
#                 numOfPhases = numOfPhases+1
#         else:
#             y-=1
#             x-=2
#             if(x>=0 or y>=0):
#                 numOfPhases = numOfPhases+1

#     return numOfPhases


# numOfPhases = calculate(x,y)
# print(numOfPhases)


import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer / denom


def main():
    k, j = input("").split()
    k = int(k)
    j = int(j)
    numSentences = 0
    while (k != 0 and j != 0 and k + j >= 3):
        numSentences += 1
        k -= 1
        j -= 1
        if (k > j):
            k -= 1
        else:
            j -= 1

    print(numSentences)


if __name__ == "__main__":
    main()
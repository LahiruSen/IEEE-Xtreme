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

# numpy and scipy are available for use
import numpy
import scipy

a = get_number()
b=a

value="yy"
strVal="y"
dict11={}
# # a=6
# # b=6
# # if(a%2==1):
# #     strVal+="Y"
if(a%2==1):
     a=a-1
else:
    a=a-2
while(a>0):
    strVal+=value
    a=a-2
if(b%2==0):
 strVal+="y"
print(strVal)

# print(a)
# print(b)
# print(value)
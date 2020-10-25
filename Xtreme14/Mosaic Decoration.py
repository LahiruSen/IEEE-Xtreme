a,b,c = map(int, input().strip().split())
values = []
for i in range(a):
    values.append(list(map(int, input().strip().split())))

x = 0
y = 0

for i in values:
    x += i[0]
    y += i[1]

tile1 = x//10
tile2 = y//10
if x%10 != 0:
    tile1+=1
if y%10 !=0:
    tile2+=1

money =  tile1*b + tile2*c
print(money)
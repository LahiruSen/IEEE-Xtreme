c, n, p, w = map(int, input().strip().split())

remainder = w % p
needed_pockets = w // p

# values = []
# for i in range(needed_pockets):
#     values.append(p)
#
# if remainder != 0:
#     values.append(remainder)
#
# # print(values)
#
# values.reverse()
if c > w:
    print(0)
elif c == w:
    print(1)

elif c > p:
    print(w // c)
elif c < p:
    # if remainder >= c:
    #     print(1)
    # else:
    #     print(2)
    empty_pockets = 0
    answer = 0
    r = 0
    released_pockets_weights = 0
    new_weight =  w
    if remainder:
        empty_pockets = n - ((w//p)+1)
    else:
        empty_pockets = n - ((w//p)+1)
    if empty_pockets > 0:
        while empty_pockets > 0 :
            released_pockets_weights = empty_pockets*c
            new_weight = w - released_pockets_weights
            mmm = released_pockets_weights
            answer += empty_pockets
            z = empty_pockets + (c*empty_pockets)//p
            rrr = (c*empty_pockets)%p
            if rrr>0:
                z+=1
            empty_pockets = n - z
            released_pockets_weights += mmm
            if answer >= n :
                print(n)
                break
        if answer < n:
            print(answer)
    else:
        print(1)



N = [int(x) for x in input().split()]
S = [int(x) for x in input().split()]
Q = [int(x) for x in input().split()]
Queries = []
for i in range(int(Q[0])):
    Queries.append(list(int(x) for x in input().split())[0])
# print(Queries)
stones = []
for i in range(N[0]):
    stones.append(i + 1)
# print(stones)
x = 0
stone_count = []
while (x < 1000):

    for i in range(len(stones)):
        # print(stones)
        ind = stones[i] - 1
        # print(ind)
        # print(ind)
        stones[i] = S[ind]
        # print("---",stones)
    x += 1
    stones = list(set(stones))
    stone_count.append(len(stones))
    # print(stones)
# print(stone_count)
for i in Queries:
    if i in stone_count:
        print(stone_count.index(i) + 1)
    else:
        print(-1)

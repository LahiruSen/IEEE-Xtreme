import itertools as itertools

import itertools as itertools


def powerset(array, K):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    ans = []
    for subset in subsets:
        if len(subset) == K:
            ans.append(subset)
    return ans

def calculate(combinations, c_wired_rooms,totalNumOfRooms):

    poweredRoomsList = []
    for combination in combinations:
        poweredRoomsList.append(calculatePoweredRooms(combination,c_wired_rooms,totalNumOfRooms))

    return max(poweredRoomsList)
    #
    # print(combinations)
    # print(c_wired_rooms)


def calculatePoweredRooms(combination,c_wired_rooms,totalNumOfRooms):
    numOfRooms = 0
    for floor in range(len(c_wired_rooms)):
        if floor in combination:
            numOfRooms += totalNumOfRooms - c_wired_rooms[floor]
        else:
            numOfRooms +=c_wired_rooms[floor]
    return numOfRooms


cases = [int(x) for x in input().split()]

for case in range(int(cases[0])):

    floors, rooms, K = [int(x) for x in input().split()]
    # print(floors,rooms,K)
    c_wired_rooms = []
    for floor in range(floors):
        c_wired = [int(x) for x in input().split()]
        c_wired_rooms.append(c_wired[0])
    # print(c_wired_rooms) # Here
    f = []
    for i in range(len(c_wired_rooms)):
        f.append(i)
        # combinations
    # combinations = list(itertools.combinations(f, K))
    combinations = powerset(f, K)

    print(calculate(combinations, c_wired_rooms,rooms))
    # print(combinations)




############################################################





# combinations = [(0,), (1,)]


# import itertools as itertools
#
#
# def addition(rooms, n):
#     return rooms - n
#
#
# cases = [int(x) for x in input().split()]
#
# for case in range(int(cases[0])):
#
#     floors, rooms, K = [int(x) for x in input().split()]
#     # print(floors,rooms,K)
#     c_wired_rooms = []
#     for floor in range(floors):
#         c_wired = [int(x) for x in input().split()]
#         c_wired_rooms.append(c_wired[0])
#     # print(c_wired_rooms) # Here
#     f = []
#     for i in range(len(c_wired_rooms)):
#         f.append(i)
#         # combinations
#     combinations = list(itertools.combinations(f, K))
#     print(combinations)
#     active_rooms_list = []
#
#     inactive_rooms = []
#     for i in c_wired_rooms:
#         inactive_rooms.append(rooms - i)
#     print(inactive_rooms)
#     get_activated = []
#     # test
#     for i in range(len(combinations)):
#         tot_activated = 0
#         for j in range(len(combinations[i])):
#             Sum = sum(c_wired_rooms) - c_wired_rooms[combinations[i][j]]
#             tot_activated += inactive_rooms[combinations[i][j]] + Sum
#         # print(tot_activated)



import read_data as rd

input_parser = rd.parser()
data = rd.get_list()

answer = 0


ans_hasmap = {'4':8}

for score_list in data:
    for score in range(score_list[0], score_list[1 + 1]):
        if (score in ans_hasmap.keys()):
            answer += ans_hasmap[score]
            continue
        ans_hasmap[score]  = get_num_ways(score)
        answer += ans_hasmap[score]

def get_num_ways(score):
    num_of_ways = 0
    ways_list = [[1] , ["x"]]
    for digit in ways_list:
        predict


def get_next_digit(currentList, score):
    if sum(currentList) < score:
        if currentList[-1] == "x":
            return [1]
        else:
            return ["x", 2*currentList[-1]]
    return False





print(data)





# def getPermutations(array):
#     permmutations = []
#     permutationHelper(array, [], permmutations)
#     return permmutations
#
#
# def permutationHelper(array, currentPermuations, permutations):
#     if not len(array) and len(currentPermuations):
#         permutations.append(currentPermuations)
#     else:
#         for i in range(len(array)):
#             newArray = array[:i] + array[i + 1:]
#             newPermutation = currentPermuations + [array[i]]
#             permutationHelper(newArray, newPermutation, permutations)

def getPermutations(array):
    permmutations = []
    permutationHelper(0, array, permmutations)
    return permmutations


def permutationHelper(i, array, permutations):
    if i == len(array)-1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationHelper(i+1, array, permutations)
            swap(array, i, j)

def swap(array, i, j):
    array[i], array[j] = array[j] , array[i]


array = [1,2,3]
print(getPermutations(array))
# N = the number of lights that are turned on in the initial configuration
# T = total number of lights
def rotate(l, n):
    return l[n:] + l[:n]

N,T = [int(x) for x in input().split()]
#print(T)
on_positions = list(int(x) for x in input().split())
#print(on_positions)
all_positions = []
for i in range(T):
    all_positions.append(i)
#print(N, T)
#print("--",all_positions)
for i in range(T):
    all_positions = rotate(all_positions,1)
    #print(all_positions)
    p_list = []
    for j in range(N):
        #print()
        #print(list(numpy.where(all_positions == on_positions[j]))[0])
        p_list.append(all_positions.index(on_positions[j]))
    #print(p_list)
    sp_list = p_list.sort()
    if sorted(p_list) == on_positions:
        break
print(i)
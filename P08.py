move_d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

pos = [0, 0]
path = []
move_history = [0]
count = 0

def move(path:list):
    count = 0
    if(len(path) == 12) :
        return 1
    start = [[0,0]]
    for i in range(len(path)):
        new_x = start[-1][0] + move_d[path[i]][0]
        new_y = start[-1][1] + move_d[path[i]][1]
        start.append([new_x, new_y])
    for i in range(len(move_d)):
        new_x = start[-1][0] + move_d[i][0]
        new_y = start[-1][1] + move_d[i][1]
        if [new_x, new_y] in start:
            pass
        else:
            new_path = path.copy()
            new_path.append(i)
            count += move(new_path)

    return count
print(move(path))
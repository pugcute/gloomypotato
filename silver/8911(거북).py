def go(position, command):
    x = position[0]
    y = position[1]
    direction = position[2]
    if command == 'F':
        if position[2] == 0:
            return [x, y+1, direction]
        elif position[2] == 1:
            return [x+1, y, direction]
        elif position[2] == 2:
            return [x, y-1, direction]
        elif position[2] == 3:
            return [x-1, y, direction]
    elif command == 'B':
        if position[2] == 0:
            return [x, y-1, direction]
        elif position[2] == 1:
            return [x-1, y, direction]
        elif position[2] == 2:
            return [x, y+1, direction]
        elif position[2] == 3:
            return [x+1, y, direction]
    elif command == 'L':
        if position[2] == 0:
            return [x, y, 3]
        elif position[2] == 1:
            return [x, y, 0]
        elif position[2] == 2:
            return [x, y, 1]
        elif position[2] == 3:
            return [x, y, 2]
    elif command == 'R':
        if position[2] == 0:
            return [x, y, 1]
        elif position[2] == 1:
            return [x, y, 2]
        elif position[2] == 2:
            return [x, y, 3]
        elif position[2] == 3:
            return [x, y, 0]

N = int(input())
for _ in range(N):
    methods = input()
    positions = [[0, 0, 0]]  # x, y, direction
    for method in methods:
        next_position = go(positions[-1], method)
        positions.append(next_position)
    positions.sort(key=lambda x:x[0])
    min_X = positions[0]
    max_X = positions[-1]
    positions.sort(key=lambda x:x[1])
    # print(positions)
    min_Y = positions[0]
    max_Y = positions[-1]
    print((max_X[0]-min_X[0]) * (max_Y[1] - min_Y[1]))


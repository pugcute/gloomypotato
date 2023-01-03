from collections import deque

def BFS(position_J, position_fire):
    answer = 'IMPOSSIBLE'
    cnt = 0
    while position_J:
        J_row, J_col = position_J.popleft()
        count_fire = len(position_fire)
        for i in range(4):
            next_J_row, next_J_col = J_row + dx[i], J_col + dy[i]
            if not 0<=next_J_row<R or not 0<=next_J_col<C:
                answer = cnt + 1
                return answer
            if 0<=next_J_row<R and 0<=next_J_col<C and metrix[next_J_row][next_J_col] == '.':
                metrix[next_J_row][next_J_col] = 'J'
                position_J.append([next_J_row, next_J_col])

        for fire_num in range(count_fire):
            fire_row, fire_col = position_fire.popleft()

            for i in range(4):
                next_fire_row, next_fire_col = fire_row + dx[i], fire_col + dy[i]
                if not 0 <= next_fire_row < R or not 0 <= next_fire_col < C:
                    continue
                if 0 <= next_fire_row < R and 0 <= fire_col < C and (metrix[next_fire_row][next_fire_col] == '.' or metrix[next_fire_row][next_fire_col] == 'J'):
                    metrix[next_fire_row][next_fire_col] = 'F'
                    position_fire.append([next_fire_row, next_fire_col])
                    listJ = list(position_J)
                    if [next_fire_row, next_fire_col] in listJ:
                        listJ.remove([next_fire_row, next_fire_col])
                    position_J = deque(listJ)
                    # for position in range(len(position_J)):
                    #     if position_J[position][0] == next_fire_row and position_J[position][1] == next_fire_col:
                    #         del position_J[position]

        cnt += 1
    return answer

R, C = map(int, input().split())
metrix = []
for _ in range(R):
    metrix.append(list(input()))

position_J = deque()
position_fire = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for row in range(R):
    for col in range(C):
        if metrix[row][col] == 'J':
            position_J.append([row, col])
        elif metrix[row][col] == 'F':
            position_fire.append([row, col])

print(BFS(position_J, position_fire))



def DFS():
    global answer
    stack = {(0, 0, matrix[0][0])}

    while stack:
        current_row, current_col, words = stack.pop()
        answer = max(answer, len(words))
        for i in range(4):
            next_row = current_row + dx[i]
            next_col = current_col + dy[i]

            if 0 <= next_row < N and 0 <= next_col < M and matrix[next_row][next_col] not in words:
                stack.add((next_row, next_col, matrix[next_row][next_col] + words))


N, M = map(int, input().split())

matrix = []
for _ in range(N):
    tmp = list(input())
    matrix.append(tmp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 1

DFS()
print(answer)

def DFS(row, col, words):
    if row >= N or col >= N:
        return
    words += matrix[row][col]
    if row == N-1 and col == N-1:
        answer.append(words)
    DFS(row+1, col, words)
    DFS(row, col+1, words)



N = int(input())
dx = [1, 0]
dy = [0, 1]
matrix = []
answer = []
for _ in range(N):
    tmp = list(input().split())
    matrix.append(tmp)

DFS(0, 0, '')

answer_num = []
for ans in answer:
    numbers = []
    operators = []
    cnt = 0
    for word in ans:
        if word not in ['+', '-', '*']:
            numbers.append(int(word))
            if operators:
                operator = operators.pop()
                if operator == '+':
                    second = numbers.pop()
                    first = numbers.pop()
                    numbers.append(first + second)
                elif operator == '-':
                    second = numbers.pop()
                    first = numbers.pop()
                    numbers.append(first - second)
                elif operator == '*':
                    second = numbers.pop()
                    first = numbers.pop()
                    numbers.append(first * second)
        else:
            operators.append(word)
        cnt += 1
        if cnt == len(ans):
            answer_num.append(numbers.pop())
            break
print(max(answer_num), min(answer_num))

import math

row, col = map(int, input().split())

answer = -1
matrix = []

for _ in range(row):
    tmp = list(input())
    matrix.append(tmp)


for current_row in range(row):
    for current_col in range(col):
        for i in range(-row, row):
            for j in range(-col, col):
                num = ''
                cr, cl = current_row, current_col
                while 0<=cr<row and 0<=cl<col:
                    num += matrix[cr][cl]
                    if i == 0 and j == 0:
                        break
                    if int(math.sqrt(int(num))) ** 2 == int(num):
                        answer = max(int(num), answer)
                    cr += i
                    cl += j

print(answer)
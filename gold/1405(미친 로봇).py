
def DFS(cnt, go_list, possible):
    global answer
    if cnt == N[0]:
        answer += possible
        return
    for i in range(4):
        next_x, next_y = go_list[-1][0] + dx[i], go_list[-1][1] + dy[i]
        if -14<=next_x<=14 and -14<=next_y<=14 and [next_x, next_y] not in go_list:
            DFS(cnt+1, go_list + [[next_x, next_y]], possible*(N[i+1] / 100))



N = list(map(int, input().split()))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
DFS(0, [[0, 0]], 1)
print(answer)

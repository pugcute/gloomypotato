from collections import deque

def BFS():

    while positions:
        start_position, time = positions.popleft()
        visited[start_position] = True

        if start_position == X:
            return time
        if start_position + 1 < 100001 and not visited[start_position + 1]:
            positions.append([start_position+1, time+1])
            visited[start_position + 1] = True
            if start_position + 1 == X:
                return time + 1
        if start_position - 1 >= 0 and not visited[start_position - 1]:
            positions.append([start_position - 1, time + 1])
            visited[start_position - 1] = True
            if start_position - 1 == X:
                return time + 1
        if start_position * 2 < 100001 and not visited[start_position * 2]:
            positions.append([start_position * 2, time + 1])
            visited[start_position * 2] = True
            if start_position * 2 == X:
                return time + 1





N, X = map(int, input().split())
positions = deque()
positions.append([N, 0])
visited = [False] * 100001

print(BFS())


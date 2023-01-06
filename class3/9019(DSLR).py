import sys
from collections import deque
sys.setrecursionlimit(10**9)

def BFS():
    global to_visits, visited, command_visited
    while True:
        flag = 0
        current = to_visits.popleft()
        visited[current] = True
        if current == end:
            break
        else:
            # str_current = str(current)
            for tmp in commands:
                if tmp == 'D':
                    next_number = (current * 2) % 10000
                    if next_number == end:
                        flag = 1
                        command_visited[next_number] += command_visited[current] + 'D'
                        break
                    if visited[next_number] is False:
                        to_visits.append(next_number)
                        visited[next_number] = True
                        command_visited[next_number] += command_visited[current] + 'D'

                elif tmp == 'S':
                    next_number = current - 1
                    if next_number == 0:
                        next_number = 9999
                    if next_number == end:
                        flag = 1
                        command_visited[next_number] += command_visited[current] + 'S'
                        break
                    if visited[next_number] is False:
                        to_visits.append(next_number)
                        visited[next_number] = True
                        command_visited[next_number] += command_visited[current] + 'S'
                elif tmp == 'L':
                    if current > 0:
                        # tmp_deque = deque(list(str_current))
                        # tmp_deque.rotate(-1)
                        # next_str = ''.join(list(tmp_deque))
                        front = current % 1000
                        back = current // 1000
                        next_number = front * 10 + back
                        if next_number == end:
                            command_visited[next_number] += command_visited[current] + 'L'
                            flag = 1
                            break
                        if visited[next_number] is False:
                            to_visits.append(next_number)
                            visited[next_number] = True
                            command_visited[next_number] += command_visited[current] + 'L'
                else:
                    if current > 0:
                        # tmp_deque = deque(list(str_current))
                        # tmp_deque.rotate(1)
                        # next_str = ''.join(list(tmp_deque))
                        # next_number = int(next_str)
                        front = current % 10
                        back = current // 10
                        next_number = front * 1000 + back

                        if next_number == end:
                            flag = 1
                            command_visited[next_number] += command_visited[current] + 'R'
                            break
                        if visited[next_number] is False:
                            to_visits.append(next_number)
                            visited[next_number] = True
                            command_visited[next_number] += command_visited[current] + 'R'
        if flag == 1:
            break
    return




N = int(input())
commands = ['D', 'S', 'L', 'R']
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    visited = [False] * 10001
    command_visited = ['']*10001
    to_visits = deque([start])

    BFS()
    print(command_visited[end])
    # print(answer)
N = int(input())
numbers = list(map(int, input().split()))

count_list = [0] * 1003

for num in numbers:
    count_list[num] += 1

current = 0
answer = []
while sum(count_list) > 0:
    if count_list[current]:
        if count_list[current + 1]:
            for next_val in range(current + 2, 1001):
                if count_list[next_val]:
                    answer.extend(count_list[current] * [current])
                    answer.append(next_val)
                    count_list[current] = 0
                    count_list[next_val] -= 1
                    break
            else:
                answer.extend(count_list[current + 1] * [current + 1])
                answer.extend(count_list[current] * [current])
                count_list[current] = 0
                count_list[current + 1] = 0

        else:
            while count_list[current]:
                answer.append(current)
                count_list[current] -= 1
    current += 1

print(*answer)
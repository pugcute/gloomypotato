
N = int(input())
building_list = list(map(int, input().split()))

answer = 0

for i in range(N):
    cnt = 0
    left = -float('inf')
    right = -float('inf')
    for left_idx in range(i-1, -1, -1):
        if (building_list[left_idx] - building_list[i])/(i - left_idx) > left:
            left = (building_list[left_idx] - building_list[i]) / (i - left_idx)
            cnt += 1

    for right_idx in range(i+1, N):
        if (building_list[right_idx] - building_list[i])/(right_idx - i) > right:
            right = (building_list[right_idx] - building_list[i]) / (right_idx - i)
            cnt += 1

    answer = max(answer, cnt)

print(answer)
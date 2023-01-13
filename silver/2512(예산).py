import sys
from bisect import bisect_left





#
# N = int(sys.stdin.readline())
# moneys = list(map(int, sys.stdin.readline().split()))
# K = int(sys.stdin.readline())

moneys = [120, 110, 140, 150]
moneys.sort()

start = 0
end = len(moneys)-1

while start <= end:
    if start > end:
        break
    mid = (start + end) // 2

    if moneys[mid] > 150:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)




# start = 1
# end = max(moneys)
#
# while start <= end:
#     result = 0
#     if start > end:
#         break
#     mid = (start + end) // 2
#     idx = bisect_left(moneys, mid)
#     result += sum(moneys[:idx])
#
#     for money in moneys[idx:]:
#         result += mid
#
#     if result > K:
#         end = mid - 1
#     else:
#         answer = mid
#         start = mid + 1
#
# print(answer)
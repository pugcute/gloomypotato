
from itertools import product


def mix_card(step, div):
    if div == 0:
        return step[::-1]
    return mix_card(step[-1 * 2 ** div:], div - 1) + step[:-1 * 2 ** div]


N = int(input())
cards = [i for i in range(1, N + 1)]
result = list(map(int, input().split()))
k = 1

while N > 1:
    k += 1
    N //= 2

for i in product([i for i in range(1, k)], repeat=2):
    if result == mix_card(mix_card(cards[:], i[0]), i[1]):
        print(*i)
        break

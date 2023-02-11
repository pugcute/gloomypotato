N = int(input())
stars = [[' '] * 2 * N for _ in range(N)]


def get_start(x, y, n):
    if n == 3:
        stars[x][y] = '*'
        stars[x + 1][y - 1] = stars[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            stars[x + 2][y + i] = '*'
    else:
        next_n = n // 2
        get_start(x, y, next_n)
        get_start(x + next_n, y - next_n, next_n)
        get_start(x + next_n, y + next_n, next_n)


get_start(0, N - 1, N)
for ans in stars:
    print("".join(ans))
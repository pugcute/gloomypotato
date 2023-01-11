
def hanoi(n, start, tmp, end):
    if n == 1:
        print(f'{start} {end}')
        return
    else:
        hanoi(n-1, start, end, tmp)
        print(f'{start} {end}')
        hanoi(n-1, tmp, start, end)
    return
N =int(input())

if N <= 20:
    print(2**N-1)
    hanoi(N, '1', '2', '3')
else:
    print(2**N-1)
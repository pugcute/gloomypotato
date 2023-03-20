
def prime_list(n):
    sosus = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sosus[i] == True:
            for j in range(i+i, n+1, i):
                sosus[j] = False
    return [i for i in range(2, n+1) if sosus[i] == True]

N = int(input())
sosus = prime_list(N)
start = 0
end = 1
if N == 1:
    print(0)
else:
    sums = sosus[start]
    answer = 0
    if sums == N:
        answer += 1

    while not (start == end == len(sosus)):
        if sums < N and end < len(sosus):
            sums += sosus[end]
            end += 1
        else:
            sums -= sosus[start]
            start += 1
        if sums == N:
            answer += 1

    print(answer)
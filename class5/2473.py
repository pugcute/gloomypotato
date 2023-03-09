N = int(input())
solutions = sorted(list(map(int, input().split())))

val = float("inf")
answer = []


if N == 3:
    print(*solutions)

else:
    for _ in range(N-2):
        solution_3 = solutions.pop()
        start, end = 0, len(solutions) - 1
        while start != end:
            tmp = solution_3 + solutions[start] + solutions[end]
            if val > abs(tmp):
                val = abs(tmp)
                answer = [solution_3, solutions[start], solutions[end]]

            if tmp < val:
                start += 1
            else:
                end -= 1

            if val == 0:
                break
        if val == 0:
            break
    print(*sorted(answer))
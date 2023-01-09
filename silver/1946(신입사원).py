import sys

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    len_employee = int(sys.stdin.readline().rstrip())
    employees = []
    for _ in range(len_employee):
        employee = list(map(int, sys.stdin.readline().split()))
        employees.append(employee)
    answer = []
    cnt = 0
    employees.sort(key=lambda x:x[0])
    answer.append(employees[0])
    for employee in employees[1:]:
        if answer[-1][1] > employee[1]:
            answer.append(employee)
    print(len(answer))
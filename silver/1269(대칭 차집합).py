
a, b = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

set_a = set(list_a)
set_b = set(list_b)

a_div = set_a - set_b
b_div = set_b - set_a


print(len(list(a_div)) + len(list(b_div)))
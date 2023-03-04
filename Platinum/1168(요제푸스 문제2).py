

def init_tree(start, end, node):
    if start == end:
        tree[node] = 1
    else:
        mid = (start + end) // 2
        tree[node] = init_tree(start, mid, node * 2) + init_tree(mid + 1, end, node * 2 + 1)
    return tree[node]


def find_index(start, end, node, command):
    if start == end:
        return start
    mid = (start + end) // 2
    if command <= tree[node * 2]:
        return find_index(start, mid, node * 2, command)
    else:
        return find_index(mid + 1, end, node * 2 + 1, command - tree[2 * node])


def change_tree(start, end, node, index):
    tree[node] -= 1
    if start == end:
        return 0
    mid = (start + end) // 2
    if index <= mid:
        return change_tree(start, mid, node * 2, index)
    else:
        return change_tree(mid + 1, end, node * 2 + 1, index)


N, K = map(int, input().split())
tree = [0] * (N * 4)
init_tree(0, N - 1, 1)
answer = []
command = 1

for i in range(N):
    command += K - 1
    tree_size = N - i

    if command % tree_size == 0:
        command = tree_size
    elif command > tree_size:
        command %= tree_size

    index = find_index(1, N, 1, command)
    change_tree(1, N, 1, index)

    answer.append(index)

print('<', end='')
for i in range(N):
    if i < N - 1:
        print(f'{answer[i]}, ', end='')
    else:
        print(f'{answer[i]}>', end='')

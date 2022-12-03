# 그냥은 안되네 내일 이분탐색하겠음
N, M = map(int, input().split())
trees = list(map(int, input().split()))

max_height = max(trees)
if max_height <= M:
    tmp_height = 0
else:
    tmp_height = max_height-M

modify_tree = []
for x in trees:
    if tmp_height < x:
        modify_tree.append(x - tmp_height)


if len(modify_tree) == 1:
    print(tmp_height)
else:
    if max_height <= M:
        tmp = sum(modify_tree) - max_height
    else:
        tmp = sum(modify_tree) - M
    print(tmp_height + int(tmp/len(modify_tree)))
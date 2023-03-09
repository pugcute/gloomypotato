def find(plane):
    if trees[plane] == plane:
        return plane
    trees[plane] = find(trees[plane])
    return trees[plane]

G = int(input())
P = int(input())
answer = 0
planes = []
for _ in range(P):
    g = int(input())
    planes.append(g)

trees = [i for i in range(G+1)]
for plane in planes:
    tmp = find(plane)
    if tmp == 0:
        break
    trees[tmp] = trees[tmp-1]
    answer += 1

print(answer)
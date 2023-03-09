N, M = map(int, input().split())

knowns = set(map(int, input()[1:].split()))

parties = []
for _ in range(M):
    party = set(map(int, input()[1:].split()))
    parties.append(party)

for _ in range(M):
    for party in parties:
        if knowns & party:
            knowns = knowns.union(party)

answer = 0
for party in parties:
    if not (knowns & party):
        answer += 1

print(answer)
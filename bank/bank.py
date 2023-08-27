N, T = list(map(int, input().split()))
people = []
for n in range(N):
    people.append(list(map(int, input().split())) + [False])

tot_money = 0

for t in range(T - 1, -1, -1):
    sav = [-1, -1]
    for (i, p) in enumerate(people):
        if p[2]:
            continue
        if p[1] < t:
            continue

        if p[0] > sav[0]:
            sav = [p[0], i]

    if sav[0] != -1:
        people[sav[1]][2] = True
        tot_money += sav[0]

print(tot_money)


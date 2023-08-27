#########################################
#
# Kattis: wheresmyinternet <https://open.kattis.com/problems/wheresmyinternet>
#
#########################################


import sys

sys.setrecursionlimit(2000000)
n, m = list(map(int, input().split()))

connections = [[] for x in range(n + 1)]

for line in range(m):
    a, b = list(map(int, input().split()))
    connections[a].append(b)
    connections[b].append(a)

vis = set()
def dfs(start):
    vis.add(start)
    for node in connections[start]:
        if node not in vis:
            dfs(node)

dfs(1)

houses = set([x for x in range(1, n + 1)])

if len(houses - vis) == 0:
    print("Connected")
else:
    for h in (houses - vis):
        print(h)

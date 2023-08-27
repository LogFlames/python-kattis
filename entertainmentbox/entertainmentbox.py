#########################
#
# Kattis: entertainmentbox <https://open.kattis.com/problems/entertainmentbox>
#
#########################

from heapq import heappush, heappop, heapify
import sys

n, k = list(map(int, input().split()))

shows = []

for line in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))

    shows.append((x, y))

tot_recorded = 0

shows.sort(key = lambda x: x[0])

rec_box = []

for show in shows:
    heappush(rec_box, -show[1])
    print("s")
    print(rec_box)

    if len(rec_box) >= k + 1 and -rec_box[k] > show[0]:
        print("a: ", heappop(rec_box))

    print(rec_box)

print(len(rec_box))







"""
box_ends = []
for b in range(k):
    heappush(box_ends, 1)

for show in shows:
    for i, box in enumerate(box_ends):
        if show[0] >= -box:
            box_ends[i] = box_ends[-1]
            box_ends.pop()
            heapify(box_ends)

            heappush(box_ends, -show[1])

            tot_recorded += 1
            break;

print(tot_recorded)
"""

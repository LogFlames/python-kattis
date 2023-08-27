N = int(input())
L = int(input())
DEBUG = True

cars = [*map(int, input().split())]

def possible(cars):

    if DEBUG: print()
    cars.sort(reverse = True)
    if DEBUG: print(len(cars))
    if DEBUG: print(cars)
    lanes = [0,0,0,0]
    for c in cars:
        print(f"{c = }")
        mi = -1
        ml = -1
        for l in range(4):
            print(f"{lanes[l] = } {L - lanes[l] = } >= {c = }")
            if lanes[l] > ml and L - lanes[l] >= c:
                ml = lanes[l]
                mi = l

        if mi != -1:
            lanes[mi] += c + 1
            if DEBUG: print(f"{lanes = }")
        else:
            if DEBUG: print(False)
            if DEBUG: print(lanes)
            return False
    if DEBUG: print(True)
    if DEBUG: print(lanes)
    return True

mp = 0
for i in range(1, len(cars) + 1):
    if possible(cars[:i]):
        mp = i

print(mp)


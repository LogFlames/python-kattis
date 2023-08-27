N = int(input())
L = int(input())

cars = [*map(int, input().split())]

max_cars = 0

def place(lanes, cars, index):
    global max_cars
    max_cars = max(max_cars, index)
    
    if index == len(cars):
        return
    
    if lanes is None:
        lanes = [L, L, L, L]
        
    for i in range(4):
        if lanes[i] >= cars[index]:
            sav = lanes[i]
            lanes[i] -= cars[index] + 1
            place(lanes, cars, index + 1)
            lanes[i] = sav
    return

place(None, cars, 0)

print(max_cars)

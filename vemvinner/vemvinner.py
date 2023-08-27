a = [input().split() for _ in range(3)]

for i in range(3):
    first = a[i][0]
    if first == "_":
        continue
    for j in range(3):
        if a[i][j] != first:
            break
    else:
        if first == "X":
            print("Johan har vunnit")
            exit()
        else:
            print("Abdullah har vunnit")
            exit()

for j in range(3):
    first = a[0][j]
    if first == "_":
        continue
    for i in range(3):
        if a[i][j] != first:
            break
    else:
        if first == "X":
            print("Johan har vunnit")
            exit()
        else:
            print("Abdullah har vunnit")
            exit()

if a[0][0] == a[1][1] == a[2][2] == "X":
    print("Johan har vunnit")
    exit()
if a[0][0] == a[1][1] == a[2][2] == "O":
    print("Abdullah har vunnit")
    exit()

if a[0][2] == a[1][1] == a[2][0] == "X":
    print("Johan har vunnit")
    exit()
if a[0][2] == a[1][1] == a[2][0] == "O":
    print("Abdullah har vunnit")
    exit()

print("ingen har vunnit")


while (n:=int(input())):
    reg = [-1]*32
    for _ in range(n):
        inst,*cells = input().split()
        if "S" in inst:
            reg[int(cells[0])] = 1
        elif "C" in inst:
            reg[int(cells[0])] = 0
        elif "D" in inst:
            if reg[int(cells[1])] == 0:
                reg[int(cells[0])] = 0
            if reg[int(cells[0])] == 1 and reg[int(cells[1])] == -1:
                reg[int(cells[0])] = -1
        elif "O" in inst:
            if reg[int(cells[1])] == 1:
                reg[int(cells[0])] = 1
            if reg[int(cells[0])] == 0 and reg[int(cells[1])] == -1:
                reg[int(cells[0])] = -1

    for r in reg[::-1]:
        if r == -1:
            print("?", end = "")
        else:
            print(r, end = "")
    print()

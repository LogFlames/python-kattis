M = int(input())

for m in range(M):
    N = int(input())
    # test which one produces n
    arr = ["+", "-", "*", "//"]
    done = False
    for a in arr:
        for b in arr:
            for c in arr:
                s = f"4 {a} 4 {b} 4 {c} 4"
                if eval(s) == N:
                    print(s.replace("//", "/") + " = " + str(eval(s)))
                    done = True
                    break
            if done:
                break
        if done:
            break
    if not done:
        print("no solution")


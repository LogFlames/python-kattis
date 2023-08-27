letters = "abcd"

alts= []
def gen(s, n):
    if n == 0:
        alts.append(s)
        return
    for l in letters:
        gen(s + l, n - 1)

with open("test.txt", "w+") as f:
    for l in range(2, 10):
        alts = []
        gen("", l)
        for g in alts:
            f.write(g + "\n")





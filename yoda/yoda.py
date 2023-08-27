a = input()[::-1]
b = input()[::-1]

a2 = ""
b2 = ""

for i in range(max(len(a), len(b))):
    if i < len(a) and ((i < len(b) and b[i] <= a[i]) or i >= len(b)):
        a2 += a[i]
    if i < len(b) and ((i < len(a) and a[i] <= b[i]) or i >= len(a)):
        b2 += b[i]

print(int(a2[::-1]) if a2 != "" else "YODA")
print(int(b2[::-1]) if b2 != "" else "YODA")

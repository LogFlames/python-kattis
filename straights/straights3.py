n=[*map(int,[*open(0)][1].split())]
n.sort()
m={}
for i in n:
 if i-1 in m and m[i-1]>0:m[i-1]-=1
 m[i]=m.get(i,0)+1
print(sum(m.values()))

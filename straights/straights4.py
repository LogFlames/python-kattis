n=[*open(0)][1].split()
m={}
for i in sorted(map(int,n)):
 if m.get(i-1,0)>0:m[i-1]-=1
 m[i]=m.get(i,0)+1
print(sum(m.values()))

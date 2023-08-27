input()
n=[*map(int,[*open(0)][1].split())]
m={i:0 for i in n}
for l in n:m[l]+=1
k=sorted(m.keys())
t=m[k[0]]
for i,p in zip(k[1:],k):
 if i-p>1:m[p]=0
 if m[i]>m[p]:t+=m[i]-m[p]
print(t)

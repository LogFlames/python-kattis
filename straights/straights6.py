n=sorted(map(int,[*open(0)][1].split()))
m=[0]*7**6
for i in n:m[i-1]-=m[i-1]>0;m[i]+=1
print(sum(m))

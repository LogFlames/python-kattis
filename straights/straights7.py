m=[0]*7**6
for i in sorted(map(int,[*open(0)][1].split())):m[i-1]-=m[i-1]>0;m[i]+=1
print(sum(m))

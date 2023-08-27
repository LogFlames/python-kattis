n=sorted(map(int,[*open(0)][1].split()))
m={}
t=0
for i in n:a=m.get(i-1,0);m[i-1]=a-(a>0);m[i]=m.get(i,0)+1;t+=a<=0
print(t)

N,K=map(int,input().split())
f=[0,1]
while len(f)<N+2:f+=[f[-1]+f[-2]]
while N>2:a=K>f[N-2];K-=f[N-2]*a;N-=2-a
print(" NA"[N])

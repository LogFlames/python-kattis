while n:=int(input()):
 r=['?']*32
 for o in'?'*n:i,*c=[*input().split(),0];a,b=map(int,c[:2]);r[a]={"S":1,"C":0,"A":[[r[a],o][(r[a],r[b])==(1,o)],0][r[b]==0],"O":[[r[a],o][(r[a],r[b])==(0,o)],1][r[b]==1]}[i[0]]
 print("".join(map(str,r[::-1])))

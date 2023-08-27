while n:=int(input()):
 r=['?']*32
 for o in'?'*n:i,*c=[*input().split(),0];a,b=map(int,c[:2]);r[a]=[[[r[a],o][(r[a],r[b])==(1,o)],0][r[b]==0],0,0,1,[[r[a],o][(r[a],r[b])==(0,o)],1][r[b]==1]][ord(i[0])%5]
 print("".join(map(str,r[::-1])))

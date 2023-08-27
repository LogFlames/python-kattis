while n:=int(input()):
 r=['?']*32
 for o in'?'*n:i,*c=[*input().split(),0];a,b=map(int,c[:2]);r[a]=[[[l:=r[a],o][(l,k:=r[b])==(1,o)],0][k==0],0,0,1,[[l,o][(l,k)==(0,o)],1][k==1]][ord(i[0])%5]
 print("".join(map(str,r[::-1])))

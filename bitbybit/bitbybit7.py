while n:=int(input()):
 r=['?']*32
 for o in'?'*n:i,*c=input().split()+[0];a,b=map(int,c[:2]);h=[l:=r[~a],o];r[~a]=[[h[(l,k:=r[~b])==(1,o)],0][k==0],0,0,1,[h[(l,k)==(0,o)],1][k==1]][ord(i[0])%5]
 print(*r,sep="")

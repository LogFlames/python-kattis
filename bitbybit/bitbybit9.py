while n:=int(input()):
 r=[3]*32
 for o in'?'*n:
     i,*c=input().split()+[0];
     a,b=map(int,c[:2]);
     r[~a]=[r[~a]*r[~b]%6,0,0,1,min(r[~a],r[~b])+r[~b]or r[~a]][ord(i[0])%5]
 print("".join("010?"[x]for x in r))


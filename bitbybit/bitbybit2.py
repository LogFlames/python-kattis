o=None
while n:=int(input()):
 r=[o]*32
 for _ in' '*n:
  i,*c=[*input().split(),0];a=int(c[0]);b=int(c[1])
  if"S"in i:r[a]=1
  if"C"in i:r[a]=0
  if"D"in i:
   if r[b]==0:r[a]=0
   if r[a]and r[b]==o:r[a]=o
  if"O"in i:
   if r[b]:r[a]=1
   if(r[a],r[b])==(0,o):r[a]=o
 print("".join(map(str,r[::-1])).replace("None","?"))

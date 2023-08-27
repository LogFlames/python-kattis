for s in[*open(0)][1:]:
 i=0
 while(s[:i]*70)[:len(s)-1]!=s[:-1]:i+=1
 print(i)

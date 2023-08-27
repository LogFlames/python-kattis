for n in' '*int(input()):a=input();j=len(a);print([i for i in range(j+1)if(a[:i]*71)[:j]==a][0])

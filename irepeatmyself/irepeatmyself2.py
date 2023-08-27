for n in' '*int(input()):
 a=input()
 print([i for i in range(len(a)+1)if(a[:i]*71)[:len(a)]==a][0])

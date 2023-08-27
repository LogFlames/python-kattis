#{*map(
#        lambda x:
#        print(" ".join([x[i] if x[i].lower() not in map(lambda y:y.lower(),x[:i]) else '.'for i in range(len(x))])),
#(lambda x:[print(" ".join([x[i] if x[i] not in map(lambda y:y.lower(),sum(x[:],[])) else "."])) for i in range(len(x[j])) for j in range(len(x))])

#(lambda b:(lambda x,a:[print(" ".join("."*(x[y].lower()in a[:y]and x[y]!='\n')or x[y]for y in range(len(x))).replace("\n ","\n"))])(b,[*map(lambda z:z.lower(),b)]))(sum([l.split()+["\n"]for l in __import__('sys').stdin],[]))

#(lambda b:(lambda x,a:print(*['.'*(x[i].lower()in a[:i])or x[i]for i in range(len(x))]))(b.split(),b.lower().split()))(__import__('sys').stdin.read())

#(lambda x:print(*['.'*(x[i]in x[:i])or x[i]for i in range(len(x))]))(open(0).read().lower().split())

#(lambda x:print(*['.'*(x.index(x[i])<i)or x[i]for i in range(len(x))]))(open(0).read().lower().split())

(lambda x:print(*['.'*(Z in x[:i])or Z for i,Z in enumerate(x)]))(open(0).read().lower().split())









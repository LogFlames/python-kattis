#for p in[[x for x in range(2,32000)if all([x%y for y in range(2,int(x**0.5)+1)])]]:[(lambda x:(lambda r,x:(print(f'{x} has {len(r)} representation(s)',*r)))([f'{a}+{x-a}'for a in p if(x-a)in p and a<=x-a],x))(int(input()))for _ in' '*int(input())]

#for p in[{x for x in range(2,2**15)if all([x%y for y in range(2,int(x**.5)+1)])}]:[*map(lambda x:(lambda r,x:(print(f'{x} has {len(r)} representation(s)',*r)))([f'{a}+{x-a}'for a in p if{x-a}&p and a<=x-a],x),map(int,open(0).readlines()[1:]))]

#for p in[{x for x in range(2,2**15)if all([x%y for y in range(2,182)if y<x])}]:[(lambda r:print(f'{x} has {len(r)} representation(s)',*r))([f'{a}+{x-a}'for a in p if{x-a}&p and a<=x-a])for x in map(int,[*open(0)][1:])]

#for p in[{x for x in range(2,2**15)if all([x%y for y in range(2,182)if y<x])}]:[(lambda r:print(f'{x} has {len(r)} representation(s)',*r))([f'{a}+{x-a}'for a in p if a<=x-a in p])for x in map(int,[*open(0)][1:])]

for p in[{x for x in range(2,2**15)if all([x%y for y in range(2,182)if y<x])}]:[(lambda r:print(f'{x} has {len(r)} representation(s)',*r))([f'{a}+{x-a}'for a in p if a<=x-a in p])for x in map(int,[*open(0)][1:])]










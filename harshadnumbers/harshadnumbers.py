#set(map(lambda x:(print(x),exit())if x%sum(map(int,str(x)))==0 else 0,range(int(input()),2000000000)))
#set((print(x),exit())for x in range(int(input()),99**9)if x%sum(map(int,str(x)))==0)
#set(map(lambda x:x%sum(map(int,str(x)))<1<exit(print(x)),range(int(input()),9**99)))
#for x in range(999):lambda y:y%sum(map(int,str(y)))or exit(print(y))(x+int(input()))
#[(exit(),print(x))for x in range(int(input()),99**9)if x%sum(map(int,str(x)))==0]
#[exit(print(x))for x in range(int(input()),99**9)if x%sum(map(int,str(x)))==0]
#[exit(print(x))for x in range(int(input()),99**9)if x%sum(map(int,str(x)))<1]
#for x in range(int(input()),99**9):x%sum(map(int,str(x)))<1==exit(print(x))
#next(print(x)for x in range(int(input()),9**99)if x%sum(map(int,str(x)))<1)
#for x in range(int(input()),99**9):x%sum(map(int,str(x)))<1<exit(print(x))

#[x%sum(map(int,str(x)))<1<exit(print(x))for x in range(int(input()),9**99)]

for x in range(int(input()),99**9):x%sum(map(int,str(x)))<1<exit(print(x))

#Tobias: for x in range(int(input()),99**9):x%sum(map(int,str(x)))or exit(print(x))

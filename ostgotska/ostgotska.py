#print(["dae ae ju traeligt va","haer talar vi rikssvenska"][(lambda x:sum("ae"in i for i in x)<.4*len(x))(input().split())])

#print(["dae ae ju traeligt va","haer talar vi rikssvenska"][(lambda x:sum("ae"in i for i in x)<.4*len(x))(input().split())])


print((lambda x:sum("ae"in i for i in x)<.4*len(x))(input().split())and"haer talar vi rikssvenska"or"dae ae ju traeligt va")

print((lambda x:sum("ae"in i for i in x)<.4*len(x))(input().split())*"haer talar vi rikssvenska"or"dae ae ju traeligt va")


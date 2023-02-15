from functools import cmp_to_key
def idx(c):
    if ord(c)>=ord('a') and ord(c)<=ord('z'):
        return ord(c)-ord('a')
    else:
        return ord(c)-ord('0')+26
def comp(x,y):
    for i,j in zip(x,y):
        if idx(i)<idx(j):
            return -1
        if idx(i)>idx(j):
            return 1
    return 0
f=open("sites.txt","r")
lines=f.readlines()
lines.sort(key=cmp_to_key(comp))
f.close()
f=open("sites.txt","w")
for line in lines:
    f.write(line)
f.close()
f=open("sites_1.txt","r")
lines=f.readlines()
lines.sort(key=cmp_to_key(comp))
f.close()
f=open("sites_1.txt","w")
for line in lines:
    f.write(line)
f.close()
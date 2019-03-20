
#1
a = [6,4,6,6,6,3,7,2,2,9,12]

b = 0
for i in a:
    b = b + i

print(b)

c = len(a)
d = b/c
print(d)

#2
e = []

for cg in a:

    e.append(cg - d)
    
print(e)

#3
f = []
for t in e:
    f.append(t**2)

print (f)

u = 0
for z in f:
    u = u + z

print(u)

gg = u/c ### gg is ***
print(gg)
    
#4
ggg = gg**0.5 ### 
print(ggg)

##### calculation of standard devoation #####


data = [6, 4, 6, 6, 6, 3, 7, 2, 2, 8]

deviation = []
deviation2 = []


s = 0
v = 0

for n in data:
    s += n
    

k = len(data)

av = s/k 
print(av)
    
for i in data:
    l = i - av 
    deviation.append(l) 


print(deviation)

    
for i in deviation:
    m = i**2
    deviation2.append(m)

print(deviation2)


for i in deviation2:
    v += i

d = v/k

print(d)

sd = d**1/2

print(sd)


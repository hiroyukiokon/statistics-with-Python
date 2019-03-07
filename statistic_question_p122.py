##### calculation of population variance and population standard devoation #####


data = [11, 9, 4, 1]

rf = [0.3, 0.3, 0.2, 0.2]

m = []

d = []
d2 = []

f = []



for i in range(0, 4):
    mf = data[i]*rf[i]
    m.append(mf)
    
    
print(m)

s = 0

for i in m:
    s += i
    
pm = s
print(pm)


    
for i in data:
    l = i - pm 
    d.append(l) 


print(d)

    
for i in d:
    m = i**2
    d2.append(m)

print(d2)


for i in range(0,4):
    ff = d2[i]*rf[i]
    f.append(ff)

print(f)

pv = 0
for i in f:
    pv += i
    

print(pv)
print(pv)


psd = pv**(1/2)

print(psd)


#ステップ１
data=[6,4,6,6,6,3,7,2,2,8]
x=0
for i in data:
    x=x+i
print(x)

l=len(data)
mean = x/l
print(mean)


#

deviation=[]

for i in data:
    deviation.append(i-mean)

print(deviation)


#
square=[]

for i in deviation:
    square.append(i**2)

print(square)

#
standarddeviation=[]

f=0
for i in square:
    f=f+i
print(f)

l=len(square)
sd =f/l
print(standarddeviation)


G=(standarddeviation**0.5)
print(G)
    

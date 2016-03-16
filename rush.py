n=[]
m=0
s=0
x=int(input())
while x!=0:
    n.append(x)
    x=int(input())
z=len(n)
for i in n:
    s+=i/len(n)
for i in n:
    m+=(i-s)**2


m=((m)/(len(n)-1))**(0.5)

print(m)
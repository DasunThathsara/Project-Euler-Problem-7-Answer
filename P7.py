w=[]
l=[]
a=10000000
b=10001
for x in range(2,a):
    print(x)
    for y in range(2,x+1):
        t=x%y
        if t==0:
            l.append(t)
    if len(l)==1:
        w.append(x)
    l.clear()
    if len(w)==b:
        break
print(w[b-1])

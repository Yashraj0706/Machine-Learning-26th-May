a=input('enter a random char:')
d={i:a.count(i) for i in a}
print(d)
b=d.values()
c=set(b)

if len(c)==1:
    print("mystring")
else:
    print("not mystring")

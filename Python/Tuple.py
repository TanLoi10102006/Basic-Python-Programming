a =(10,20,5,7,8)
print(type(a))
print(a)
for i in a:
    print(i)
print(10 in a)
print(a.count(10))
b=(9,4,5,6,7)
print(a+b)
print(max(a))
print(min(b))
print(sum(a))

# sắp xếp có 2 cách 
c=sorted(a)
print(c)
d =list(b)
d.sort()
print(d)

# unpacking và unpacking*
preson =("Loi",20,1.65)
name,age,height=preson
print(name)
print(age)
print(height)

aaa=(1,"Loi",20,1.65)
nunber,*bb=aaa
print(nunber)
print(bb)



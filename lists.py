x=3
print(type(x))

x=str(3)
print(type(x))

a="Sanjana"
for i in a:
    print(i)

print("length of string",len(a))

a="My name is Sanjana"
print(a[:7])
print(a[11:18])

print(type(a))

print(a.upper())

txt="My name is \"Sanjana\" Kote"
print(txt)

a=["joe","joy","kote"]
a.insert(1,"ram")
print(a)

b=["lamp","kite","time"]
c=a+b
print(c)

a.extend(b)
print(a)

l=(b.pop(1))
print(b)
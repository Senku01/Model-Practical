import array

s1= array.array('i',[1,2,4])
s2= array.array('i',[3,5,6])

print(s1)
print(s2)
s3=s1+s2
print(s3)
s1.append(4)
print(s1)
s1.insert(0,10)
print(s1)
s1.extend(s2)
print(s2)

a=[8,6,5,4]
print("before Pop",len(a))
a.pop()
print("After pop",len(a))

for v in a:
    print(v)
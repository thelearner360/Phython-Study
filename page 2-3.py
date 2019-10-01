# 1
odd = [1, 3, 5, 7, 9]
print (odd)

a = []
print (a)

b = [1, 2, 3]
print (b)

# 2

a = [1, 2, 3, 4, 5]
print (a[0:2])

b = a[:2]
c = a[2:]

print (b)
print (c)

# 3

a = [345, 666, 777, 233, 4423, 222, 15]
print (a[2:5])
print (a[:4])
print (a[3:])
print (a[-6:-3])
print (a[-6:5])

# 4

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)


# 5

a = [1, 2, 3]
print (a * 3)


# 6

a = [1, 2, 3]
a[2] = 4
print (a)

# 7

a = [345, 666, 777, 233, 4423, 222, 15]
print (a[2:5])

a[2:5] = ["X", "Q", "RRR", 4345, 334]
print (a)

a[-6:4] = ["GOOD"]
print (a)

a[-7:] = []
print (a)

# 8

a = [1, "A", "B", "C", 4]
print (a[1:3])

a[1:3] = []
print(a)

del a[1:]
print (a)

# 9

a = [233,23, 2354, 75, 886, 80]
a.append(40)
print (a)

a.sort()
print (a)

a.sort(reverse = True)
print (a)

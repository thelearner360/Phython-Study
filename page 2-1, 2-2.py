# 1
a = 3
b = 4
print(a + b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)
print(a // b)
print(7 % 3)

# 2

print("hello world")
print("phython is fun")

print("""life is too short,
you need phython""")

print('''life" is'
too short,
you need phython''')

# 3

food = "phython's favorite food is perl"
print(food)

food = 'phython\'s favorite food is perl'
print(food)

say = '"phython is very easy." he says'
print(say)

say = "\"phython is very easy.\" he says"
print(say)

# 4
multiline = '''life is too shot
you need phython'''
print(multiline)

multiline = "life is too shor\nyou need phython"
print(multiline)

# 5

head = "phython "
tail = "is fun"

print(head + tail)

# 6
a = "phython"

print(a * 2)

# 7

a = "hello world"

print (a[0])
print (a[-11])
print (a[10])
print (a[-1])

print(a[0:5])

print(a[6:])

print(a[:])

print(a[-11:-6])

print(a[-5:-2])

print(a[-5:9])

# 8

A = Life is too short, you need phython

print(A[2])
print(A[12])
print(A[23])

# 9

a = "20010331Raniy"

year = a[0:4] # 또는 a[:4]
month = a[4:6]
day = a[6:8]
weather = a[8 : 13] # 또는 a[8:]

print(year + "년" + month + "월" + day + "일" + weather + "입니다")

# 10

s = "I eat %d apples." % 3
print(s)

s = "I ate % d apples, so I was sick for %s days" % (10, "three")
print(s)


# 11

s = "%10s" % "HI"
print("[" + s + "]")

s = "% - 10sjane." % "HI"
print("[" + s +"]")

s = "%0.4f" % 3.142134234
print(s)

s = "%10.4f" % 3.42134234
print(s)

# 12

a = "hobby"
print(a.count("b"))

a = "Phython is best choice"
print(a.find("b"))
print(a.find("k"))

print(a.index("b"))
print(a.index("k"))

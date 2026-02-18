fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = []
for x in fruits:
  if "a" in x:
    newlist1.append(x)
print(newlist1)

newlist2 = [x for x in fruits if "a" in x]
print(newlist2)

newlist3 = [x for x in fruits if x != "apple"]
print(newlist3)

newlist4 = [x for x in fruits]
print(newlist4)

newlist5 = [x for x in fruits]
print(newlist5)

newlist6 = [x for x in range(10) if x < 5]
print(newlist6)

newlist7 = [x.upper() for x in fruits]
print(newlist7)

newlist8 = ['hello' for x in fruits]
print(newlist8)

newlist9 = [x if x != "banana" else "orange" for x in fruits]
print(newlist9)
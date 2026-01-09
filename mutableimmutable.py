x = 5
y = 10
print(id(x), id(y))
y += 1
print( x, y)
print(id(x), id(y))


list1=[1, 2, 3, 4, 5]
list2=[6, 7, 8, 9, 10]

print(id(list1,id(list2)))
list1.append(11)
print(id(list1), id(list2))

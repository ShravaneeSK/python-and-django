import copy
a = [[1, 2], [3, 4]]

b=a.copy()

c=copy.deepcopy(a)


a[0][0]=15
print("a:", a)
print("b:", b)
print("c:", c)
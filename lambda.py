
def a_first(a):
    return a[1]

a= [[1,4], [5,6], [8,14]]
a.sort(key = a_first)
print(a)
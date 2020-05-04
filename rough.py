list1 = range(10)
list2 = range(10)
def fun(a, b):
    return a == b
out = map(fun, list1, list2)

print(out)

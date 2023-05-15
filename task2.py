list = [21, 22, 23, 24, 25]
list2 = [22, 24, 26,28,30]
list3 = list + list2
print(list3)

def countX(list3, x):
    count = 0
    for ele in list3:
        if (ele == x):
            count = count + 1
    return count
x = 24
print(countX(list3, x))

list3.reverse()
print(list3)

list3.sort()
print(list3)

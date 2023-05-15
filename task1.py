fruits = [ ]
fruits.extend(["apple", "orange", "banana", "pineapple", "watermelon", "kiwi"])
print(len(fruits))
print(fruits[3])
print(fruits[-3])
fruits.append("strawberry")
a1 = fruits[0]
a2 =  fruits[1]
al = fruits[5]
ar = fruits[2:5]
a1,a2,*ar,al = fruits
print(a1,a2,ar,al)
print(fruits[1:4])

if "banana"in fruits :
    print ("Banana Exists")
if "mango" in fruits:
    print("Mango is present in list")

fruits[1]= "banana"
fruits[2] = "orange"
print(fruits)

fruits= fruits[:-1]
print("deleted list", fruits)

x = fruits.remove("pineapple")
print("removed pineapple in list", fruits)

fruits.pop(1)
print(fruits)

fruits.clear()
print("list is cleared",fruits)

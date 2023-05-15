#creation of list
x = [1,2,3,4,5]
print(x)
#applying the append method to list
x.append(7)
print("append data:",x)
#applying the extend method to list
x.extend([8,9])
print("extend data:",x)
#applying the remove method to list
x.remove(9)
print("remove data:",x)
#applying the reverse method to list
x.reverse()
print("reverse data:",x)
#arranging list in assending order
print("assending")
print(sorted(x))
#arranging list in descending order
print("descending")
x.sort(reverse=True)
print(x)


#part-2
# printing list 5 time
list1=[1,2,3,4,["python","java","c++",[10,20,30]],5,6,7,["apple","banana","orange"]]
print("\n",list1*5)

#finding and printing python from the list of list
#for orange
print("\n",list1[8][2])

#for python
print(list1[4][0])


#part3
# copy a list using slice function
print("\n copy of a list using slice function=\n",slice(list1))




#part-4
#Create a tuple and apply different type of mathematical operation on it (Sum, Maximum, minimum etc.).
#creation of tuple
tuple1 = (1, 5, 7, 9, 3,9)
print("\ntuple element is:",tuple1)
#mathematical function on tuple

#1. len function
print("length of tuple is:",len(tuple1))

#2.maximum and minimum function in tuple
print("maximum of tuple is:",max(tuple1))
print("minimum of tuple is:",min(tuple1))

#3.sum of tupple
print("sum of tuple:",sum(tuple1))

#4. sort for tuple
print("sorting:",sorted(tuple1))

#5. count function on tuple
print("counting of element 9 in tuple:",tuple1.count(9))



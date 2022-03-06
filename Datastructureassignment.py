#====================================================================
#program 1
#assigning elements to different lists
#====================================================================

list1=["a","b","c",1,23,4]
list2=["a1","b1","c1","2a"]
list3=["ram","shyam","ghanshyam"]
print("the lists in first place were: \n", list1, "\n", list2,"\n",list3)
# prints the original list


list1.insert(4,"pankaj")
list2.insert(1,"2b")
list3.insert(2,"radheshyam")
print("list after assigning elements to different lists: \n",list1, "\n", list2,"\n",list3,)
#=============================================================================================


#====================================================================
#program 2
#accessing elements from a tuple
#====================================================================
tup1=("a","b","c","d")
tup2=("1","2","3","4","5")

print(tup1[1])
#accessing second element of the tuple 1 by index 1
print(tup2[3])
#accessing second element of the tuple 2 by index 3



#====================================================================
#program 3
#deleting different dictionary elements
#====================================================================

d1={"a":1,"b":2,"c":3}
print(d1)

del d1["b"]
print(d1)

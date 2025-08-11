#Create an empty list

my_list = []


#Create an empty list

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
 

# Insert 15 at index 1

my_list.insert(1, 15) 
 

# Extend my_list with [50, 60, 70]

my_list2 = [50,60,70]
my_list.extend(my_list2)


#Remove the last element

del my_list[7]

#alternatives

#my_list.remove("70")
#my_list.pop()


#Sort in Ascending order

my_list.sort()


#Find and print index of 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)


#Print the finalized list
print(my_list)
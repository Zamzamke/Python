#create an empty list called my_list
my_list = []

#append the following elements to my list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#insert the value 15 at the second position in my_list
my_list.insert(1, 15)
print(my_list)

#extend my_list with another list:[50,60,70]
my_list.extend([50, 60, 70])
print(my_list)

#remove the last statement from my_list
my_list.pop()
print(my_list)

#sort my_list in ascending order
my_list.sort()
print(my_list)

#find and print hte index of the value 30 in my_list
print(my_list.index(30))

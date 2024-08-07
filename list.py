tea_varities = ["green tea" , "black tea" , "boba tea", "masala tea"] #list is like string it is mutable 

tea_varities[1:2] = ["konsi bhi chai"]  # replacing element in list
print(tea_varities) 

tea_varities[1:2] = ["oolong tea"]

print(tea_varities)

tea_varities[1:1] = ["tea", "chaha"] #inserting element in list

print(tea_varities) 

tea_varities.append("japanese tea") # insert element at last of the list

print(tea_varities)

tea_varities.pop() # remove last element
print(tea_varities)

tea_varities.remove("green tea") # remove disired element
print(tea_varities)

tea_varities.insert(1 ,"hehe")# inserting at a specfic index
print(tea_varities)


tea_varities_copy = tea_varities.copy()#copy the list 
tea_varities_copy.append("lemon")
print(tea_varities_copy)
print(tea_varities)

squared_num = [x**2 for x in range(10)] #damm python is op
print(squared_num)

cub_num = [y**3 for y in range(10)]
print(cub_num)

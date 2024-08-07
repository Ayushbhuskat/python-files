#dictionary is a special datatypes

chai = {"masala" : "spicy","ginger": "zesty", "green": "mild"}

print(chai.get("masala"))
chai["green"]= "fresh"
print(chai)

for tea in chai :
    print(tea)

for tea in chai :           #for key value pair
    print(tea,chai[tea])

for key , value in chai.items() : # another method for key values in dictionary
    print(key , value)

if "masala" in chai :
    print("masala chai is present")

print(len(chai))

chai["earl grey"] = "citrus"  # inserting key value pair
print(chai)

chai.pop("earl grey")  # delete disered key value pair
print(chai)

chai.popitem() # delete last key value pair
print(chai)

del chai["ginger"]
print(chai)

chai_copy = chai.copy()#copy 

#dicitnory ke ander dicitnory

Tea_shop = {
    "chai" : {"masala" : "spicy" , "ginger": "zesty"},
   " tea" :  {"green": "fresh", "black": "strong"}
           }
print(Tea_shop)
print(Tea_shop["chai"])

#{{}, {}}  matrix

squared_num = { x : x**2 for x in range(6)}
print(squared_num)
squared_num.clear() # clears the dict
print(squared_num)

# another way 
keys = ["masala", "ginger", "lemon"]
default_value =  "delicious"
new_dict = dict.fromkeys(keys,keys)
print(new_dict)
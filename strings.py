#multiline strings in python

apple = '''hello,my name is ayush
i am 20 year old and doing engineering 
thank you'''

print(apple)

name = "ayush"

print(name[0])#indexing in string


for character in name : print(character)

for character in apple : print(character)


#slicing in strings

fruit = "Mango"

print(len(fruit))


print(fruit[0:5])
print(fruit[:5])
print(fruit[0:len(fruit)-3])#-ve indexing
print(fruit[-3:-1])



#string methods
#STRINGS ARE IMMUTABLE
a = "ayush!!!!" 
print(a.upper())
print(a.rstrip("!"))#remove trailing character
print(a.replace("ayush","AYUSH"))

#some methods- split() , capitalize() , center() , count() , endswith() , find() , index() , isalnum() , isalpha() , isprintable(), isspace()

'''typecasting is of two types
1.explicit typecasting (user gives intrustion)
2.implicit typecasting (done by py lang itself) '''

#explicit 
a = "12"
b = "12"

print(int(a) + int(b))

#explicit
string = "15"
number = 7
string_number = int(string)
sum = number + string_number
print(sum)

#implicit
a = 1.5
b = 1
print(a + b)
a = int(input("enter the age "))

if(a <= 13):
    print("you are age group is child")
elif( a > 13 and a <= 19):
    print("you are teenager")
elif( a >= 20 and  a<= 59):
    print("you are Adult")
else:
    print("you are senior")
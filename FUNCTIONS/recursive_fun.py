#recursion is like chakraviv we need to know the exit point 
def factorial(n):
    if n == 0 :
        return 1
    else:
        return (n)*factorial(n-1)
    
num = factorial(3)
print(num)
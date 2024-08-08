import math
def circle (radius) :
    area = math.pi*radius**2
    circumfrence = 2*math.pi*radius
    return round(area) , round(circumfrence) 

a,c= circle(3)
print("area: ",a , "cirumfernec : ",c)
def equilateral(sides):
    a , b, c = sorted (sides)
    if (a == b == c) and (a > 0 and b >0 and c >0) : 
        return True 
    else : 
        return False 


def isosceles(sides):
    a, b, c = sorted (sides)
    if (a + b >= c and b + c >= a and a + c >= b) and (a == b or a==c or b == c) : 
        return True
    else : 
        return False


def scalene(sides):
    a, b,c = sorted (sides)
    if (a + b >= c and b + c >= a and a + c >= b) and (a!= b != c) : 
        return True
    else : 
        return False

    
    
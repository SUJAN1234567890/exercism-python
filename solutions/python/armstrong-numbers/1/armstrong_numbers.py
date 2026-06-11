def is_armstrong_number(number):
    length = len(str(number))
    digits = [int(char) for char in str (number)]
    sum = 0
    for item in digits : 
        sum = sum + item ** length
    
    if sum == number : 
        return True
    else : 
        return False

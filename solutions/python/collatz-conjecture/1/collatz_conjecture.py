def steps(number):
    if number > 1 :
        i = 0
        while True : 
            if number %2 == 0 : 
                number = number /2 
            else : 
                number = 3 * number + 1
            
            i += 1
            if number == 1 : 
                break 

        return i
    elif number == 1 : 
        return 0
    else : 
        raise ValueError ("Only positive integers are allowed")

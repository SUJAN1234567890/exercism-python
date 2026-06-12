def is_valid(isbn):
    clean_isbn = isbn.replace("-", "")
    if len(clean_isbn) == 10 : 
        numbers = "0123456789"
        i = 10
        sum = 0
        if clean_isbn[-1] == "X" : 
            for n in clean_isbn[0:len(clean_isbn) - 1] : 
                if n in numbers : 
                    sum = sum + int(n) * i 
                    i = i - 1
                elif n not in numbers : 
                    return False
            sum = sum + 10 * 1 
        elif "X" in clean_isbn : 
            return False 
        else : 
            for n in clean_isbn : 
                if n in numbers : 
                    sum = sum + int(n) * i 
                    i = i - 1
                elif n not in numbers : 
                    return False

        if sum % 11 == 0 : 
            return True
        return False
    else : 
        return False

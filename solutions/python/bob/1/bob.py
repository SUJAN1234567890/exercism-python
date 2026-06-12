def response(hey_bob):
    x = hey_bob.strip()
    if x == "" : 
        return "Fine. Be that way!"
    elif "?" in x[-1] and x.isupper() == False : 
        return "Sure."
    elif "?" not in x[-1] and x.isupper() == True  :
        return "Whoa, chill out!"
    elif "?" in x[-1] and x.isupper() == True : 
        return "Calm down, I know what I'm doing!"
    else : 
        return "Whatever."

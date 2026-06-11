def is_isogram(string):
    string = string.lower()
    l = list(string)
    l2 = []
    for item in l : 
        if item != " "  and item != "-": 
            l2.append(item)

    if len(l2) == len (set (l2)) : 
        return True
    return False


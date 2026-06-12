def rotate(text, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    part1 = alphabets[key:]
    part2 = alphabets[:key]
    rotate_alphabets = part1 + part2
    l = []
    for item in text : 
        if item in alphabets : 
            position_of_item = alphabets.find(item) 
            new_item = rotate_alphabets[position_of_item]
            l.append(new_item)
        elif item not in alphabets : 
            if item.isupper() == True :
                position_of_item = alphabets.find(item.lower())
                new_item = rotate_alphabets[position_of_item].upper()
                l.append(new_item)
            else : 
                l.append(item)
    new = "".join(l)
    return new
def commands(binary_str):
    l = []
    library = {
        1 : "wink",
        2 : "double blink",
        3 : "close your eyes",
        4 : "jump",
    }
    r = binary_str[-1:-6:-1]
    for index , item in enumerate(r) :
        if int(item) == 1 : 
            if index != 4 : 
                l.append(library[index + 1])
            elif index == 4 : 
                l.reverse()
    return l

          


def find(search_list, value):
    search_list = sorted(search_list)
    left_index = 0 
    right_index = len(search_list) -1 
    while left_index <= right_index: 
        middle = (left_index + right_index) //2
        if search_list[middle] == value : 
            break
        elif value > search_list[middle] :
            left_index = middle +1
        elif value < search_list[middle] : 
            right_index = middle - 1
    else : 
        raise ValueError("value not in array")
    return middle
library = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9"
    }


def label(colors):
    num = int (library[colors[0]] + library[colors[1]])
    power = int(library[colors[2]])
    num = num * (10 ** power)
    number_of_Zeroes = str(num).count("0")

    if number_of_Zeroes >=9 :
        return f"{int (num/(10**9))} gigaohms"
    elif number_of_Zeroes >= 6 : 
        return f"{int (num/(10**6))} megaohms"
    elif number_of_Zeroes >= 3 : 
        return f"{int (num/(10**3))} kiloohms"
    else : 
        return f"{num} ohms"
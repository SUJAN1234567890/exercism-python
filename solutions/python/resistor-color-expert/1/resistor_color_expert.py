def resistor_label(colors) :
    library1 = {
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

    library2 = {
        "grey" : "0.05%",
        "violet" : "0.1%",
        "blue" : "0.25%",
        "green" : "0.5%",
        "brown" : "1%",
        "red" : "2%",
        "gold" : "5%",
        "silver" : "10%"
    }

    if len(colors) == 4 :
        num = int (library1[colors[0]] + library1[colors[1]])
        power = int(library1[colors[2]])
        tolerance = library2[colors[3]]
        num = num * (10 ** power)
        number_of_Zeroes = str(num).count("0")

        if (number_of_Zeroes >=9 and (num/(10 ** 9)) < 1) or (number_of_Zeroes >=6 and (num /(10 ** 9)) >= 1) :
            return f"{(num/(10**9)):g} gigaohms ±{tolerance}"
        elif (number_of_Zeroes >= 6 and (num / (10 ** 6)) < 1) or (number_of_Zeroes >=3 and (num / (10 ** 6)) >= 1) : 
            return f"{(num/(10**6)):g} megaohms ±{tolerance}"
        elif (number_of_Zeroes >= 3 and (num / (10 ** 3)) < 1) or ((num / (10 ** 3)) >= 1): 
            return f"{(num/(10**3)):g} kiloohms ±{tolerance}"
        else : 
            return f"{num} ohms ±{tolerance}"
    
    elif len(colors) == 5 :
        num = int(library1[colors[0]] + library1[colors[1]] + library1[colors[2]])
        power = int (library1[colors[3]])
        tolerance = library2[colors[4]]
        num = num * (10 ** power)
        number_of_Zeroes = str(num).count("0")

        if (number_of_Zeroes >=9 and (num/(10 ** 9)) < 1) or (number_of_Zeroes >=6 and (num /(10 ** 9)) >= 1) :
            return f"{(num/(10**9)):g} gigaohms ±{tolerance}"
        elif (number_of_Zeroes >= 6 and (num / (10 ** 6)) < 1) or (number_of_Zeroes >=3 and (num / (10 ** 6)) >= 1) : 
            return f"{(num/(10**6)):g} megaohms ±{tolerance}"
        elif (number_of_Zeroes >= 3 and (num / (10 ** 3)) < 1) or ((num / (10 ** 3)) >= 1): 
            return f"{(num/(10**3)):g} kiloohms ±{tolerance}"
        else : 
            return f"{num} ohms ±{tolerance}"
    
    elif len(colors) == 1 and "black" in colors : 
        return "0 ohms"

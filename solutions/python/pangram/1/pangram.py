def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = sentence.lower()

    for item in alphabet : 
        if item not in s : 
            return False 
    return True

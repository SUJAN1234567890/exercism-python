def find_anagrams(word, candidates):
    expected = []
    word_lower = word.lower()
    list_word = sorted(word_lower)
    for item in candidates :
        item_lower = item.lower ()
        list_item = sorted(item_lower)
        if word_lower == item_lower :
            continue
        elif list_item == list_word : 
            expected.append(item)
        else : 
            continue
    return expected   
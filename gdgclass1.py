def exercise(value):
    freq = {}
    for char in value:
        freq[char] = freq.get(char, 0) + 1
    return freq

    
    # freq = {}
    # for char in value:
    #     if freq.get(char) == None:
    #         freq.update({char:1})
    #     else:
    #         current_count = freq.get(char)
    #         freq.update({char:current_count+1})
    # return freq

test = exercise("aaabbc")
print(test)          



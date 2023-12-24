def find_index(word, d):
    for index, element in enumerate(d):
        if word == element:
            return index
    return -1
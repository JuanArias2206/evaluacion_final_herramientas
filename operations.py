def get_ascii(word):
    return ord(word)
    
def get_binary(code):
    binary = format(code, "08b")
    return binary
    
def getResults(lists):
    concatenated = []
    for sublist in lists:
        concatenated.extend(sublist)
    return concatenated
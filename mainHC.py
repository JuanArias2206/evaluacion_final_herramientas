from operations import get_ascii, get_binary, getResults
import sys

menu = int(input("Menu\n=====\n1. Character\n2. Word"))

if (menu == 1):
    char = input("Enter a character: ")
    word = char
    code = get_ascii(word)
    binary = get_binary(code)
    print('Results\n======')
    print('ASCII character value of "{0}" is {1}'.format(word, code))
    print('Total: ', end='')
    for element in binary:
        print(element, end='')
    print()
    
elif(menu == 2):
    word = input("Enter a word: ")
    lists = []
    i = 0
    print('Results\n======')
    for char in word:
        code = get_ascii(char)
        print('ASCII character value of "{0}" is {1}'.format(char, code))
        binary = get_binary(code)
        lists.append(binary)
    result = getResults(lists)
    
    print('Total: ', end='')
    for element in result:
        print(element, end='')
    print()
else:
    sys.exit()

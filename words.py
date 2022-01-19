def print_upper_words1(words):
    """Converts each word in list to uppercase and prints out each word on a separate line 
    >>> print_upper_words1(["hello", "hey", "goodbye", "yo", "yes"]) will print:
    HELLO
    HEY
    GOODBYE
    YO
    YES
    """
    for word in words:
        print(word.upper())



def print_upper_words2(words):
    """Prints words from the list that start with the letter "e" (either upper or lowercase)
    >>>print_upper_words2(["hello", "engine", "goodbye", "Eye", "yes"]) will print:
    ENGINE
    EYE
    """
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word)



def print_upper_words3(words, must_start_with):
    """ Converts to uppercase and prints words from the list that begin with the letters specified
    >>print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
    must_start_with={"h", "y"}) prints
    HELLO
    HEY
    YO
    YES
    """
          
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())


print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
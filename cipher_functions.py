"""CSC108 Assignment 2 functions"""

from typing import List


ENCRYPT = 'e'
DECRYPT = 'd'


def clean_message(message: str) -> str:
    """Return a string with only uppercase letters from message with non-
    alphabetic characters removed.
    
    >>> clean_message('Hello world!')
    'HELLOWORLD'
    >>> clean_message("Python? It's my favourite language.")
    'PYTHONITSMYFAVOURITELANGUAGE'
    >>> clean_message('88test')
    'TEST'
    
    Precondition: message cannot be None
    """
    
    edited_message = ""
    for char in message:
        if char.isalpha():
            char = char.upper()
            edited_message += char
    return edited_message


def encrypt_letter(letter: str, keystream_value: int) -> str:
    """Return a string with letter converted to an encrypted letter by adding 
    the keystream_value to its unencrypted ascii number to obtain it's encrypted 
    ascii number then converting back to a letter
    
    >>> encrypt_letter("B", 3) 
    'E'
    >>> encrypt_letter("Z", 1)
    'A'
    
    Precondition: letter is a valid letter in the alphabet, keystream_value is
    less than or equal to 26 
    """
    
    encrypted_value = ord(letter) - 64 + keystream_value
    if encrypted_value > 26:
        encrypted_value = encrypted_value % 26
    encrypted_letter = chr(encrypted_value + 64)
    return encrypted_letter
    
    
def decrypt_letter(letter: str, keystream_value: int) -> str:
    
    """Return a string with letter decrypted by subtracting the keystream value 
    from the encrypted ascii number of a letter to get the decrypted ascii 
    number of the letter then converting it back to a letter
    
    >>> decrypt_letter('A',1)
    'Z'
    >>> decrypt_letter('E',3)
    'B'
    
    Precondition: The letter must be a valid letter in the English alphabet and 
    the keystream_value must be less than or equal to 26
    """
    
    decrypted_value = ord(letter) - 64 - keystream_value
    if decrypted_value < 1:
        decrypted_value = decrypted_value + 26
    decrypted_letter = chr(decrypted_value + 64)
    return decrypted_letter


def is_valid_deck(deck: List[int]) -> bool:
    """Return a boolean telling the computer whether deck is valid or not based 
    on if all numbers from range 1-28 are contained in deck or not
    
    >>> is_valid_deck([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28])
    True
    >>> is_valid_deck([1,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28])
    False
    
    Precondition: The size of the deck is always 28  
    """
    
    for i in range(1, 29):
        if not i in deck:
            return False
    return True
    
    
def swap_cards(deck: List[int], index: int) -> None:
    """Swap the card at the index provided with the card before it in the list
    
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28]
    >>> swap_cards(deck, 1)
    >>> deck
    [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> swap_cards(deck, 0)
    >>> deck
    [28, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 2]
    
    Precondition: deck is a valid deck with at least 2 elements, the index is a 
    valid index from 0 to len(deck)-1
    """
    
    index_card = deck[index]
    if index == 0:
        previous_index = len(deck) - 1
    else:
        previous_index = index - 1
    deck[index] = deck[previous_index]
    deck[previous_index] = index_card
    
    
def find_high_and_second_high_values(deck: List[int]) -> List[int]:
    """Return the a list of the values of the second highest and highest cards
    
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> find_high_and_second_high_values(deck)
    [28, 27]
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29]
    >>> find_high_and_second_high_values(deck)
    [29, 28]
    
    Precondition: deck is a valid deck with at least two elements
    """
    
    highest_value = 0
    second_highest_value = 0
    for i in deck:
        if i > highest_value:
            second_highest_value = highest_value
            highest_value = i
        elif i > second_highest_value:
            second_highest_value = i
    list_of_highs = [highest_value, second_highest_value]
    return list_of_highs
    
    
def get_small_joker_value(deck: List[int]) -> int:
    """Return the value of the smallest joker (the second highest card)
    
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> get_small_joker_value(deck)
    27
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29]
    >>> get_small_joker_value(deck)
    28
    
    Precondition: deck is a valid deck with at least two elements
    """
    
    a_list_of_highs = find_high_and_second_high_values(deck)
    return a_list_of_highs[1]


def get_big_joker_value(deck: List[int]) -> int:
    """Return the value of the biggest joker (the highest card)
    
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> get_big_joker_value(deck)
    28
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29]
    >>> get_big_joker_value(deck)
    29
    
    Precondition: deck is a valid deck with at least two elements
    """
    
    a_list_of_highs = find_high_and_second_high_values(deck)
    return a_list_of_highs[0]


def move_small_joker(deck: List[int]) -> None:
    """Mutate the deck by swapping the small joker with the card directly before 
    in the deck
    
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> move_small_joker(deck)
    >>> deck
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 26, 28]
    >>> move_small_joker(deck)
    >>> deck
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 25, 26, 28]
    
    Precondition: deck is a valid deck and the second highest card occurs once
    """
    
    small_joker_value = get_small_joker_value(deck)
    index_of_small_joker = find_index_of_card(deck, small_joker_value)
    swap_cards(deck, index_of_small_joker)


def find_index_of_card(deck: List[int], card_value: int) -> int:
    """Return the index of card value in deck.
    
    >>> deck = [28, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1]
    >>> find_index_of_card(deck, 28)
    0
    >>> find_index_of_card(deck, 27)
    26
    
    Precondition: deck is a valid deck and the card appears once
    """
    
    index_card_value = -1
    for i in range(len(deck)):
        if deck[i] == card_value:
            index_card_value = i    
    return index_card_value
    
    
def move_big_joker(deck: List[int]) -> None:
    """Mutate the deck by swapping the big joker twice, each time with the card
    before it.
    
    >>> deck = [28, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1]
    >>> move_big_joker(deck)
    >>> deck
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 27]
    >>> move_big_joker(deck)
    >>> deck
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 28, 25, 26, 27]
    
    Precondition: deck is a valid deck and the big joker appears once
    """
    
    big_joker_value = get_big_joker_value(deck)
    index_of_big_joker = find_index_of_card(deck, big_joker_value)
    swap_cards(deck, index_of_big_joker)
    index_of_big_joker = find_index_of_card(deck, big_joker_value)
    swap_cards(deck, index_of_big_joker)


def triple_cut(deck: List[int]) -> None:
    """Modifies the deck by swapping the cards before the first occurence of a 
    joker with the cards after the second occurence of a joker
    
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 27, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 28, 25, 26]
    >>> triple_cut(deck)
    >>> deck
    [25, 26, 27, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 28, 1, 2, 3, 4, 5, 6, 7]
    
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 27, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 28, 24, 25, 26]
    >>> triple_cut(deck)
    >>> deck
    [24, 25, 26, 27, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 28, 1, 2, 3, 4, 5, 6, 7, 8]
    
    Precondition: deck is a valid deck with at exactly two jokers
    """
    
    a_list_of_highs = find_high_and_second_high_values(deck)
    big_joker = a_list_of_highs[0]
    small_joker = a_list_of_highs[1]
    counter = 0
    index_of_first = -1
    index_of_second = -1
    for i in range(len(deck)):
        if (deck[i] == big_joker or deck[i] == small_joker) and counter == 0:
            index_of_first = i
            counter = counter + 1
        elif (deck[i] == big_joker or deck[i] == small_joker) and counter == 1:
            index_of_second = i    
    first_section = deck[:index_of_first]
    second_section = deck[index_of_first: index_of_second + 1]
    if (index_of_second) == (len(deck) - 1):
        third_section = []
    else:
        third_section = deck[index_of_second + 1:]
    for i in range(len(deck)):
        deck.pop()
    deck.extend(third_section + second_section + first_section)
   
    
def insert_top_to_bottom(deck: List[int]) -> None:
    """Modify the deck by taking the number of cards represented by the value of
    the last card from the top and moving it before the last card
    
    >>> deck = [25, 26, 27, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 28, 1, 2, 3, 4, 5, 6, 7]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 28, 1, 2, 3, 4, 5, 6, 25, 26, 27, 8, 9, 10, 11, 7]
    >>> deck = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 28, 1, 2, 3, 4, 5, 6, 25, 26, 27, 8, 9, 10, 11, 7]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [19, 20, 21, 22, 23, 24, 28, 1, 2, 3, 4, 5, 6, 25, 26, 27, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 7]
    
    Precondition: deck is a valid deck with at least two elements
    """
    
    a_list_of_highs = find_high_and_second_high_values(deck)
    last_card = deck.pop()
    if last_card == a_list_of_highs[0]:
        last_card = a_list_of_highs[1]
    top = deck[:last_card]
    for i in range(last_card):
        deck.pop(i-i)
    deck.extend(top)
    deck.extend([last_card])
    
    
def get_card_at_top_index(deck: List[int]) -> int:
    """Return the value of the card at the index indicated by the value of the
    top card in deck
    
    >>> deck = [25, 26, 27, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 28, 1, 2, 3, 4, 5, 6, 7]
    >>> get_card_at_top_index(deck)
    5
    >>> deck = [28, 26, 27, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 1, 2, 3, 4, 5, 6, 7]
    >>> get_card_at_top_index(deck)
    7
    
    Precondition: The deck is be a valid deck with at least two elements.
    """
    
    a_list_of_highs = find_high_and_second_high_values(deck)
    top_card = deck[0]
    if top_card == a_list_of_highs[0]:
        top_card = a_list_of_highs[1]
    return deck[top_card]
  
  
def get_next_keystream_value(deck: List[int]) -> int:
    """Return an int representing a valid keystream value, repeat the first five
    steps until a valid keystream value is produced.
    
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_keystream_value(deck)
    3
    >>> deck = [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 5, 8, 11, 14, 17, 20, 6]
    >>> get_next_keystream_value(deck)
    4
    
    Precondition: deck is a valid deck with at least two elements
    """
    
    a_list_of_highs = find_high_and_second_high_values(deck)
    big_joker_value = a_list_of_highs[0]
    small_joker_value = a_list_of_highs[1]
    keystream = big_joker_value
    while (keystream == big_joker_value) or (keystream == small_joker_value):
        move_small_joker(deck)
        move_big_joker(deck)
        triple_cut(deck)
        insert_top_to_bottom(deck)
        keystream = get_card_at_top_index(deck)
    return keystream


def process_messages(deck: List[int], messages: List[str], action: str) -> None:
    """Return a list of messages representing the messages modified according to 
    action with keystream_values generated using deck.
    
    >>> process_messages([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], ["a7b%c","d7e*f "], 'e')
    ['TSA', 'SJR']
    >>> process_messages([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], ['T S6%A','S8*J R'], 'd')
    ['ABC', 'DEF']
    
    Precondition: the deck is a valid deck with at least two elements, 
    action is either 'e' or 'd'
    """
    
    result = []
    for message in messages:
        new_message = ""
        cleaned_message = clean_message(message)
        for letter in cleaned_message:
            keystream = get_next_keystream_value(deck)
            if action == ENCRYPT:
                new_message = new_message + encrypt_letter(letter, keystream)
            else:
                new_message = new_message + decrypt_letter(letter, keystream)
        result.extend([new_message])
    return result
    
    
if __name__ == '__main__':
    """Did you know that you can get Python to automatically run and check
    your docstring examples? These examples are called "doctests".

    To make this happen, just run this file! The two lines below do all
    the work.

    For each doctest, Python does the function call and then compares the
    output to your expected result.
    
    NOTE: your docstrings MUST be properly formatted for this to work!
    In particular, you need a space after each >>>. Otherwise Python won't
    be able to detect the example.
    """

    import doctest
    doctest.testmod()
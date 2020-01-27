"""Starter code for CSC108 Assignment 1 Winter 2018"""

# Game setting constants
SECTION_LENGTH = 3
ANSWER = 'CATDOGFOXEMU'

# Move constants
SWAP = 'S'
ROTATE = 'R'
CHECK = 'C'

def get_section_start(section_num: int) -> int:
    """ Return the starting index of the section corresponding to section_num.
    
    >>> get_section_start(1)
    0
    >>> get_section_start(3)
    6
    """
   
    return SECTION_LENGTH * (section_num - 1) 
    
def is_valid_move(move: str) -> bool:
    """Returns True if move is valid and false otherwise.
    
    >>>is_valid_move("S")
    True
    >>>is_valid_move("K")
    FALSE
    """
    
    if move == SWAP or move == ROTATE or move == CHECK:
        return True
    return False

def is_valid_section(section_num: int) -> bool:
    """Return True if the section_num is less than the maximum number of section 
    lengths and part section lengths that make up ANSWER
    >>>is_valid_section(-1)
    False
    >>>is_valid_section(4)
    True
    """
    
    #get the whole number of sub sections in the word 
    num_sub_sec = len(ANSWER) // SECTION_LENGTH 
    
    if section_num > 0 and num_sub_sec >= section_num:    
        return True
    return False

def check_section(game_state: str, section_num: int) -> bool:
    """Return True if the part of the string game_state indicated by section_num 
    is the same as the part of string ANSWER using same section_num and False '
    otherwise
    Precondition: the section_number is valid
    >>>check_section("CATDOGFOXEMU",4)
    True
    >>>check_section("CATDOGFOXEMZ",4)
    False
    """
    
    
    #rounds the maximum number of sections up to the nearest interger because need 
    #to include an example like 4.25 sections
    max_num_sec = len(ANSWER) // SECTION_LENGTH + 1    
    
    #check if the starting index, and every index up to the SECTION_LENGTH past 
    #starting index is same as in the ANSWER
    
    #if it is the last section of the word, then check everything up until the end of the word
    if section_num == max_num_sec - 1:
        return game_state[get_section_start(section_num):] == ANSWER[get_section_start(section_num):]
    
    #if it isn't the last section, check everything up to SECTION_LENGTH past 
    #starting index
    return game_state[get_section_start(section_num): get_section_start(section_num) + SECTION_LENGTH] == ANSWER[get_section_start(section_num): get_section_start(section_num) + SECTION_LENGTH]
        
def change_state(game_state: str, section_num: int, move: str) -> str:
    """Return a string with the move applied on the section of game_state indicated by the 
    section_num: if R, then move last letters of section to front, keep everything else
    same, if S, swap the first and last letters of section
    Pre-condition: the section number is valid
    >>>change_state("CATDOGFOXEMU",4,'R')
    "CATDOGFOXUEM"
    >>>change_state("CATDOGFOXUEM",3,'S')
    "CATDOGXOFUEM"
    """
    
    #for this particular function, compute the last sub section by counting all the whole sections
    last_section = len(game_state) // SECTION_LENGTH   
    
    #get the first index of sub section
    first = get_section_start(section_num)
    
    
    #get the first character
    first_character = game_state[first]
    
    #determine whether the sub section is at end or not at end of word, then:
    if last_section == section_num:
        #get the last index when the sub section is the last sub section
        last = len(game_state) - 1
    else:
        #get the last index when the sub section is somewhere at middle or beginning
        last = first + SECTION_LENGTH - 1
    
    #get last character
    last_character = game_state[last]      
        
    #store the new game_state
    new_state = ""     
    
    #if move is swap, then swap the last and first characters of sub section
    if move == SWAP:
        
        #build a new game_state switching last character and first characters
        for i in range(len(game_state)):
            if i == last:
                new_state += first_character
            elif i == first:
                new_state += last_character
            else:
                new_state += game_state[i]
    
    #if move is rotate, then move the last character to the front of subsection, moving
    #all the other index elements of sub section up one
    elif move == ROTATE:
        
        #build a new game_state moving the every element past start of sub section up one space
        #until the last index of sub section (go backwards from end to beginning)
        for i in range(len(game_state)):
            if i == first:
                new_state += last_character
            elif i == first + 1:
                new_state += first_character
            elif i>first and i<= last:
                new_state += game_state[i-1]
            else:
                new_state += game_state[i]
                
    return new_state
    

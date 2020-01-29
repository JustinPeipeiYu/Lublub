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
   
   #like saying finding what multiple of section length we start on (k.i.m. start = 0)
    return SECTION_LENGTH * (section_num - 1) 
    
def is_valid_move(move: str) -> bool:
    """Returns True if move is valid and false otherwise.
    
    >>>is_valid_move("S")
    True
    >>>is_valid_move("K")
    FALSE
    """
    
    #if any of them are true, then we return true otherwise false
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
    
    #if it's withen the range of 0 to the max number of sections, it is a valid section
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
    
    #compute the whole number of sub sections in the word
    num_sub_sec = len(ANSWER) // SECTION_LENGTH     
    
    #compute the start index of substring to be compared
    start = get_section_start(section_num)
    
    #if it is the last section of the word, then check the substring up until the end of the word
    if section_num == num_sub_sec:
        return game_state[start:] == ANSWER[start:]
    
    #check if a substring consisting of the start index and the SECTION_LENGTH past 
    #starting index is same as in the ANSWER
    return game_state[start: start + SECTION_LENGTH] == ANSWER[start: start + SECTION_LENGTH]
        
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
            elif i>first and i<= last:
                new_state += game_state[i-1]
            else:
                new_state += game_state[i]
                
    return new_state
    
def get_move_hint(game_state: str,section_num :int) -> str:
    """Return hints to rearrange the sub section of game_state indicated by section_num
    until it matches that same sub section of ANSWER
    >>>get_move_hint("CATDOGFOXMUE",4)
    S
    >>>get_move_hint("CATDOGFOXEUM",4)
    S
    """
    
    #compute the start index of game sub section using section num
    start = get_section_start(section_num)
    
    #compute the end index of game sub section using section num and length of 3
    end = start + 3
    
    #get the sub section of game_state and compare to that of ANSWER
    game_section = game_state[start:end] 
    answer_section = ANSWER[start:end]
    
    #variable to store output 
    hint = ""
    
    #compare the middle character, if it is right, just swap once to get to answer  
    if game_section[1] == answer_section[1]:
        hint = "S"
    else:
        #if the first character needs to be moved to middle, suggest rotate 
        if game_section[0] == answer_section[1]:
            hint = "R"
        #if the third character needs to be moved to middle, suggest  or rotate
        elif game_section[2] == answer_section[1]:
            #if the middle character needs to be moved to front, suggest rotate
            if game_section[1] == answer_section[0]:
                hint = "R"
            #if the middle character needs to be moved to the end, suggest swap
            else:   
                hint = "S"
    
    return hint
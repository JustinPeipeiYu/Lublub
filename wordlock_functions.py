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
    
    #rounds the maximum number of sections up to the nearest interger because need 
    #to include an example like 4.25 sections
    max_num_sec = len(ANSWER) // SECTION_LENGTH + 1
    
    if section_num > 0 and max_num_sec > section_num:    
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
    >>>change_state("CATDOGFOXUEM",4,'R')
    "CATDOGFOXMUE"
    """
    
    #for this particular function, the max of the sections is not needed to be rounded up
    max_num_sec = len(ANSWER) / SECTION_LENGTH    
    
    #get the starting index
    start = get_section_start(section_num)
    
    
    #if it is the last section
    if section_num == max_num_sec:
        #let memory variable c hold the last term of the section
        c = game_state[len(game_state)-1]
        d = SECTION_LENGTH - 1
    elif section_num <= max_num_sec:    
        #let variable d hold the length of the section minus first term
        d = len(game_state)-section_num * SECTION_LENGTH - 1        
    else:
        #let memory variable c hold the last term of the section by adding the section length minus 1
        c = game_state[start + SECTION_LENGTH - 1]
        #let d hold the length of the last section minus first term
        d = SECTION_LENGTH - 1 
    
    #run the move
    if move == ROTATE:
            #go through every element from the starting index to the end and move it
            #to the right one place
            #if we have two numbers to swap, we only want to move one up then place
            #the other down
            
            for i in range(0,d):
                print(start + d - i)
                #start at the last element and move the element before it to it's spot
                game_state[start + d - i] = game_state[start + d -1 - i]
                #move the last element to the front of section
                
                game_state[start] = c                  
              
    if move == SWAP:
            #Make the first item of section last
            game_state[start + d + 1] = game_start[start]
            #Make the last item of section first
            game_state[start] = c
    
    
    
    #return the game state with the modifications
    return game_state
    
"""Helper functions for the poetry.py program.
"""

from typing import List
from typing import Tuple
from typing import Dict

from poetry_constants import (
    CLEAN_POEM, WORD_PHONEMES, LINE_PRONUNCIATION, POEM_PRONUNCIATION,
    PRONOUNCING_DICTIONARY)

# ===================== Helper Functions =====================


def clean_word(s: str) -> str:
    """Return a new string based on s in which all letters have been converted
    to uppercase and whitespace and punctuation characters have been stripped
    from both ends. Inner punctuation and whitespace is left untouched.

    Precondition: s should not contain digits, or any unnecessary punctuation
    internal to the word.
    
    >>> clean_word('Birthday!!!')
    'BIRTHDAY'
    >>> clean_word('  "Quoted?"\\n\\n\\n')
    'QUOTED'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r """
    result = s.upper().strip(punctuation)
    return result


def split_by_newline(raw_poem: str) -> List[str]:
    r"""Return a list of the lines seperated by new line characters.
    
    Precondition: raw_poem contains lines seperated only by newline characters.
    
    >>> split_by_newline('The first line leads off,\n\n\nWith a gap before the next.\n    Then the poem ends.\n')
    ['The first line leads off,', '', '', 'With a gap before the next.', '    Then the poem ends.', '']
    >>> split_by_newline('I am Fred.\nI am twelve years old.\n\nSincerely,\n\nFred')
    ['I am Fred.', 'I am twelve years old.', '', 'Sincerely,', '', 'Fred']
    """
    lines = raw_poem.split("\n")
    return lines
    
def remove_empty_lines(lines: List[str]) -> List[str]:
    r"""Return a list of the lines with empty lines removed.
    
    Precondition: The list contains only strings and empty strings.
    
    >>> remove_empty_lines(['The first line leads off,', '', '', 'With a gap before the next.', '     Then the poem ends.', ''])
    ['The first line leads off,', 'With a gap before the next.', '     Then the poem ends.']
    >>> remove_empty_lines(['I am Fred.', 'I am twelve years old.', '', 'Sincerely,', '', 'Fred'])
    ['I am Fred.', 'I am twelve years old.', 'Sincerely,', 'Fred']
    """
    non_empty_lines = []
    for line in lines:
        if line != "":
            non_empty_lines.append(line)
    return non_empty_lines

def break_apart_by_space(non_empty_lines: List[str]) -> List[List[str]]:
    r"""Return a list of the lines broken apart by spaces to create a list 
    of words for each line.
    
    Precondition: The list contains all non-empty strings.
    
    >>> break_apart_by_space(['The first line leads off,', 'With a gap before the next.', '     Then the poem ends.   '])
    [['The', 'first', 'line', 'leads', 'off,'], ['With', 'a', 'gap', 'before', 'the', 'next.'], ['Then', 'the', 'poem', 'ends.']]
    >>> break_apart_by_space(['I am Fred.', 'I am twelve years old.', 'Sincerely,', 'Fred'])
    [['I', 'am', 'Fred.'], ['I', 'am', 'twelve', 'years', 'old.'], ['Sincerely,'], ['Fred']]
    """
    
    lists_of_words = []
    for list_of_words in non_empty_lines:
        lists_of_words.append(list_of_words.split())
    return lists_of_words

def clean_poem(raw_poem: str) -> CLEAN_POEM:
    r"""Return the non-blank, non-empty lines of poem, with whitespace removed
    from the beginning and end of each line and all words capitalized.
    
    Precondition: The raw poem has to have lines seperated by the newline character.
    
    >>> clean_poem('The first line leads off,\n\n\nWith a gap before the next.\n    Then the poem ends.\n')
    [['THE', 'FIRST', 'LINE', 'LEADS', 'OFF'], ['WITH', 'A', 'GAP', 'BEFORE', 'THE', 'NEXT'], ['THEN', 'THE', 'POEM', 'ENDS']]
    >>> clean_poem('I am Fred.\nI am twelve years old.\n\nSincerely,\n\nFred')
    [['I', 'AM', 'FRED'], ['I', 'AM', 'TWELVE', 'YEARS', 'OLD'], ['SINCERELY'], ['FRED']]
    """
    
    list_of_lines = split_by_newline(raw_poem)
    list_of_non_empty_lines = remove_empty_lines(list_of_lines)
    lists_of_words = break_apart_by_space(list_of_non_empty_lines)
    cleaned_list_of_words = []
    for word_list in lists_of_words:
        cleaned_word_list = []
        for word in word_list:
            cleaned_word_list.append(clean_word(word))
        cleaned_list_of_words.append(cleaned_word_list)
    return cleaned_list_of_words


def extract_phonemes(
        cleaned_poem: CLEAN_POEM,
        word_to_phonemes: PRONOUNCING_DICTIONARY) -> POEM_PRONUNCIATION:
    r"""Return a list where each inner list contains the phonemes for the
    corresponding line of cleaned_poem, based on the word_to_phonemes
    pronouncing dictionary.

    Precondition: Each word in the cleaned poem is a key in the word to 
    phoneme dictionary.
    
    >>> word_to_phonemes = {'YES': ['Y', 'EH1', 'S'], 'NO': ['N', 'OW1']}
    >>> extract_phonemes([['YES'], ['NO', 'YES']], word_to_phonemes)
    [[['Y', 'EH1', 'S']], [['N', 'OW1'], ['Y', 'EH1', 'S']]]
    >>> word_to_phonemes = {'HI': ['HH', 'AY1'], 'BYE': ['B', 'AY1']}
    >>> extract_phonemes([['HI'], ['HI', 'BYE']], word_to_phonemes)
    [[['HH', 'AY1']], [['HH', 'AY1'], ['B', 'AY1']]]
    """
    
    poem_of_phonemes = []
    for line in cleaned_poem:
        line_of_phonemes = []
        for word in line:
            line_of_phonemes.append(word_to_phonemes[word])
        poem_of_phonemes.append(line_of_phonemes)
    return poem_of_phonemes

def phonemes_to_str(poem_pronunciation: POEM_PRONUNCIATION) -> str:
    r"""Return a string containing all the phonemes in each word in each line in
    poem_pronunciation. The phonemes are separated by spaces, the words are
    separated by ' | ', and the lines are separated by '\\n'.

    Precondition: There is at least one word/phoneme/line in poem pronunciation list.
    
    >>> phonemes_to_str([[['Y', 'EH1', 'S']], [['N', 'OW1'], ['Y', 'EH1', 'S']]])
    'Y EH1 S\nN OW1 | Y EH1 S'
    >>> phonemes_to_str([[['HH', 'AY1']], [['HH', 'AY1'], ['B', 'AY1']]])
    'HH AY1\nHH AY1 | B AY1'
    """
    
    poem_joined = []
    for line in poem_pronunciation:
        list_of_words = []
        for word in line:
            word_joined = " ".join(word)
            list_of_words.append(word_joined)
        one_line = " | ".join(list_of_words)
        poem_joined.append(one_line)
    return "\n".join(poem_joined)

def get_common_last_syllables(
        poem_pronunciation: POEM_PRONUNCIATION) -> Dict[str, List[int]]:
    r"""Return a dictionary of syllables as the keys with values as a list of all 
    the line numbers that share that common syllable as the last syllable.
    
    Precondition: There is at least one line/word/phoneme in poem_pronunciation.
    
    >>> get_common_last_syllables([[['IH0', 'N']], [['S', 'IH0', 'N']]])
    {'IHN': [1, 2]}
    >>> get_common_last_syllables([[['HH', 'AY1']], [['B', 'AY1']]])
    {'AY': [1, 2]}
    """
    
    line_number = 0
    syllables_to_rhyme = {}
    for line in poem_pronunciation:
        syllable_counter = -1
        last_syllable = line[-1][syllable_counter]
        while not last_syllable[-1] in '1234567890':
            syllable_counter -= 1
            last_syllable = line[-1][syllable_counter]
        line_number += 1
        if syllable_counter != -1:
            ending_phoneme = last_syllable[:-1] + line[-1][-1]
        else:
            ending_phoneme = last_syllable[:-1]
        if not ending_phoneme in syllables_to_rhyme:
            syllables_to_rhyme[ending_phoneme] = [line_number]
        else:
            syllables_to_rhyme[ending_phoneme].append(line_number)    
    return syllables_to_rhyme    

def get_common_rhymes(
        common_syllables: Dict[str, List[int]]) -> Dict[str, List[int]]:
    r"""Return a dictionary with rhyme letters corresponding to different syllables
    as keys and the values are all the lines with that common rhyme letter.
    
    Precondition: There is at least one syllable in common_syllables with at least
    one line with that syllable.
    
    >>> get_common_rhymes({'IH': [1, 2]})
    {'A': [1, 2]}
    >>> get_common_rhymes({'IH': [1, 2], 'AH': [3,4]})
    {'A': [1, 2], 'B': [3, 4]}
    """
    
    rhymes_and_lines = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    syllables = []
    for key in common_syllables:
        syllables.append(key)  
    for i in range(len(syllables)):
        rhymes_and_lines[alphabet[i]] = common_syllables[syllables[i]]
    return rhymes_and_lines
        
def get_rhyme_scheme(poem_pronunciation: POEM_PRONUNCIATION) -> List[str]:
    r"""Return a list of last syllables from the poem described by
    poem_pronunction.

    Precondition: poem_pronunciation is not empty and each PHONEMES list
    contains at least one vowel phoneme.

    >>> get_rhyme_scheme([[['IH0', 'N']], [['S', 'IH0', 'N']]])
    ['A', 'A']
    >>> get_rhyme_scheme([[['IH0', 'N']], [['S', 'IH0', 'N']], [['T','AH0']], [['H', 'AH0']]])
    ['A', 'A', 'B', 'B']
    """
    
    rhymes_with_lines = get_common_rhymes(
        get_common_last_syllables(poem_pronunciation))
    rhyme_letter_keys = []
    output = []
    for key in rhymes_with_lines:
        rhyme_letter_keys.append(key)
    for i in range(len(poem_pronunciation)):
        for key in rhyme_letter_keys:
            for line in rhymes_with_lines[key]:
                if (i + 1) == line:
                    output.append(key)
    return output

def get_num_syllables(poem_pronunciation: POEM_PRONUNCIATION) -> List[int]:
    r"""Return a list of the number of syllables in each poem_pronunciation
    line.
    
    Precondition: poem_ponunciation has at least one phoneme which is a syllable.
    
    >>> get_num_syllables([[['IH0', 'N']], [['S', 'IH0', 'N']]])
    [1, 1]
    >>> get_num_syllables([[['IH0', 'N']], [['S', 'IH0', 'N']], [['T','AH0'], ['H', 'AH0']]])
    [1, 1, 2]
    """
    
    syllables_for_lines = []
    for line in poem_pronunciation:
        number_of_syllables = 0
        for word in line:
            for phoneme in word:
                if phoneme[-1] in '0123456789':
                    number_of_syllables += 1
        syllables_for_lines.append(number_of_syllables)
    return syllables_for_lines


if __name__ == '__main__':
    import doctest

    doctest.testmod()
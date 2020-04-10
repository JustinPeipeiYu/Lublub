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

    >>> clean_word('Birthday!!!')
    'BIRTHDAY'
    >>> clean_word('  "Quoted?"\\n\\n\\n')
    'QUOTED'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r """
    result = s.upper().strip(punctuation)
    return result


def split_by_newline(raw_poem: str) -> List[str]:
    """Return a list of the lines seperated by new line characters.
    
    >>> split_by_newline('The first line leads off,\n\n\nWith a gap before the next.\n    Then the poem ends.\n')
    ['The first line leads off,', '', '', 'With a gap before the next.', '     Then the poem ends.', '']
    """
    lines = raw_poem.split("\n")
    return lines
    
def remove_empty_lines(lines: List[str]) -> List[str]:
    """Return a list of the lines with empty lines removed.
    
    >>>remove_empty_lines(['The first line leads off,', '', '', 'With a gap before the next.', '     Then the poem ends.', ''])
    ['The first line leads off,', 'With a gap before the next.', '     Then the poem ends.']
    """
    non_empty_lines = []
    for line in lines:
        if line != "":
            non_empty_lines.append(line)
    return non_empty_lines

def break_apart_by_space(non_empty_lines: List[str]) -> List[List[str]]:
    """Return a list of the lines broken apart by spaces to create a list 
    of words for each line.
    
    >>>break_apart_by_space(['The first line leads off,', 'With a gap before the next.', '     Then the poem ends.'])
    [['The', 'first', 'line', 'leads', 'off,'], ['With', 'a', 'gap', 'before', 'the', 'next.'], ['     Then', 'the', 'poem', 'ends.']]
    """
    
    lists_of_words = []
    for list_of_words in non_empty_lines:
        lists_of_words.append(list_of_words.split())
    return lists_of_words

def clean_poem(raw_poem: str) -> CLEAN_POEM:
    """Return the non-blank, non-empty lines of poem, with whitespace removed
    from the beginning and end of each line and all words capitalized.

    >>> clean_poem('The first line leads off,\n\n\nWith a gap before the next.\n    Then the poem ends.\n')
    [['THE', 'FIRST', 'LINE', 'LEADS', 'OFF'], ['WITH', 'A', 'GAP', 'BEFORE', 'THE', 'NEXT'], ['THEN', 'THE', 'POEM', 'ENDS']]
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
    """Return a list where each inner list contains the phonemes for the
    corresponding line of cleaned_poem, based on the word_to_phonemes
    pronouncing dictionary.

    >>> word_to_phonemes = {'YES': ['Y', 'EH1', 'S'], 'NO': ['N', 'OW1']}
    >>> extract_phonemes([['YES'], ['NO', 'YES']], word_to_phonemes)
    [[['Y', 'EH1', 'S']], [['N', 'OW1'], ['Y', 'EH1', 'S']]]
    """
    pass


def phonemes_to_str(poem_pronunciation: POEM_PRONUNCIATION) -> str:
    """Return a string containing all the phonemes in each word in each line in
    poem_pronunciation. The phonemes are separated by spaces, the words are
    separated by ' | ', and the lines are separated by '\n'.

    >>> phonemes_to_str([[['Y', 'EH1', 'S']], [['N', 'OW1'], ['Y', 'EH1', 'S']]])
    'Y EH1 S\\nN OW1 | Y EH1 S'
    """
    pass


def get_rhyme_scheme(poem_pronunciation: POEM_PRONUNCIATION) -> List[str]:
    """Return a list of last syllables from the poem described by
    poem_pronunction.

    Precondition: poem_pronunciation is not empty and each PHONEMES list
    contains at least one vowel phoneme.

    >>> get_rhyme_scheme([[['IH0', 'N']], [['S', 'IH0', 'N']]])
    ['A', 'A']
    """
    pass


def get_num_syllables(poem_pronunciation: POEM_PRONUNCIATION) -> List[int]:
    """Return a list of the number of syllables in each poem_pronunciation
    line.
    """
    pass

'''
if __name__ == '__main__':
    import doctest

    doctest.testmod()
'''
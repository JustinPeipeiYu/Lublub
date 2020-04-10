"""Helper functions for the poetry.py program.
"""

from typing import List
from typing import Tuple
from typing import Dict

from poetry_constants import (
    CLEAN_POEM, WORD_PHONEMES, LINE_PRONUNCIATION, POEM_PRONUNCIATION,
    PRONOUNCING_DICTIONARY)

from poetry_reader import (
    SAMPLE_POETRY_FORM_FILE, EXPECTED_POETRY_FORMS, SAMPLE_DICTIONARY_FILE,
    EXPECTED_DICTIONARY, SAMPLE_POEM_FILE, read_and_trim_whitespace, 
    read_pronouncing_dictionary, read_poetry_form_descriptions,
    read_poetry_form_description 
)
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
    
    poem_of_phonemes = []
    for line in cleaned_poem:
        line_of_phonemes = []
        for word in line:
            line_of_phonemes.append(word_to_phonemes[word])
        poem_of_phonemes.append(line_of_phonemes)
    return poem_of_phonemes

def phonemes_to_str(poem_pronunciation: POEM_PRONUNCIATION) -> str:
    """Return a string containing all the phonemes in each word in each line in
    poem_pronunciation. The phonemes are separated by spaces, the words are
    separated by ' | ', and the lines are separated by '\n'.

    >>> phonemes_to_str([[['Y', 'EH1', 'S']], [['N', 'OW1'], ['Y', 'EH1', 'S']]])
    'Y EH1 S\nN OW1 | Y EH1 S'
    """
    
    poem_joined = []
    for line in poem_pronunciation:
        list_of_word_joined = []
        for word in line:
            word_joined = " ".join(word)
            list_of_word_joined.append(word_joined)
        one_list = " | ".join(list_of_word_joined)
        poem_joined.append(one_list)
    return "\n".join(poem_joined)

def get_common_last_syllables(poem_pronunciation: POEM_PRONUNCIATION) -> Dict[str, List[int]]:
    """Return a dictionary of syllables as the keys with values as a list of all the line numbers
    that share that common syllable as the last syllable.
    
    >>> get_common_last_syllables([[['IH0', 'N']], [['S', 'IH0', 'N']]])
    {'IH': [1, 2]}
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
        if not last_syllable[:-1] in syllables_to_rhyme:
            syllables_to_rhyme[last_syllable[:-1]] = [line_number]
        else:
            syllables_to_rhyme[last_syllable[:-1]].append(line_number)    
    return syllables_to_rhyme    

def get_rhyme_scheme(poem_pronunciation: POEM_PRONUNCIATION) -> List[str]:
    """Return a list of last syllables from the poem described by
    poem_pronunction.

    Precondition: poem_pronunciation is not empty and each PHONEMES list
    contains at least one vowel phoneme.

    >>> get_rhyme_scheme([[['IH0', 'N']], [['S', 'IH0', 'N']]])
    ['A', 'A']
    """
    

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
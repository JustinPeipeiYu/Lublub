"""Functions for reading the pronouncing dictionary and the poetry forms files
"""
from typing import TextIO
from typing import List
from typing import Tuple


from poetry_constants import (
    # CLEAN_POEM, WORD_PHONEMES, LINE_PRONUNCIATION, POEM_PRONUNCIATION,
    PRONOUNCING_DICTIONARY, POETRY_FORM, POETRY_FORMS)

SAMPLE_POETRY_FORM_FILE = '''Limerick
8 A
8 A
5 B
5 B
8 A

Haiku
5 *
7 * 
5 *
'''

SAMPLE_POETRY_FORM_FILE_2 = '''Haiku
5 *
7 * 
5 *

Limerick
8 A
8 A
5 B
5 B
8 A
'''


EXPECTED_POETRY_FORMS = {
    'Limerick': ([8, 8, 5, 5, 8], ['A', 'A', 'B', 'B', 'A']),
    'Haiku': ([5, 7, 5], ['*', '*', '*'])
}

EXPECTED_POETRY_FORMS_2 = {
    'Haiku': ([5, 7, 5], ['*', '*', '*']),
    'Limerick': ([8, 8, 5, 5, 8], ['A', 'A', 'B', 'B', 'A'])
}

SAMPLE_DICTIONARY_FILE = ''';;; Comment line
ABSINTHE  AE1 B S IH0 N TH
HEART  HH AA1 R T
FONDER  F AA1 N D ER0
'''

SAMPLE_DICTIONARY_FILE_2 = ''';;; Comment line
HEART  HH AA1 R T
FONDER  F AA1 N D ER0
ABSINTHE  AE1 B S IH0 N TH
'''

EXPECTED_DICTIONARY_2 = {
    'HEART': ['HH', 'AA1', 'R', 'T', ],
    'FONDER': ['F', 'AA1', 'N', 'D', 'ER0'],
    'ABSINTHE': ['AE1', 'B', 'S', 'IH0', 'N', 'TH']
}

EXPECTED_DICTIONARY = {
    'ABSINTHE': ['AE1', 'B', 'S', 'IH0', 'N', 'TH'],
    'HEART': ['HH', 'AA1', 'R', 'T', ],
    'FONDER': ['F', 'AA1', 'N', 'D', 'ER0']
}

SAMPLE_POEM_FILE = '''  Is this mic on?

Get off my lawn.
'''

SAMPLE_POEM_FILE_2 = ''' Hey you my name is Joe.

I heard my name on the radio.
'''

def read_and_trim_whitespace(poem_file: TextIO) -> str:
    """Return a string containing the poem in poem_file, with
    blank lines and leading and trailing whitespace removed.
    >>> import io
    >>> poem_file = io.StringIO(SAMPLE_POEM_FILE)
    >>> read_and_trim_whitespace(poem_file)
    'Is this mic on?\\n\\nGet off my lawn.'
    >>> import io
    >>> poem_file_2 = io.StringIO(SAMPLE_POEM_FILE_2)
    >>> read_and_trim_whitespace(poem_file_2)
    'Hey you my name is Joe.\\n\\nI heard my name on the radio.'
    
    Precondition: The poem file must contain each new idea on a new line.
    """
    poem = ""
    for line in poem_file.readlines():
        poem += line.strip() + "\n"
    return poem.strip()


def read_pronouncing_dictionary(
        pronunciation_file: TextIO) -> PRONOUNCING_DICTIONARY:
    """Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.
    >>> import io
    >>> dict_file = io.StringIO(SAMPLE_DICTIONARY_FILE)
    >>> result = read_pronouncing_dictionary(dict_file)
    >>> result == EXPECTED_DICTIONARY
    True
    >>> import io
    >>> dict_file_2 = io.StringIO(SAMPLE_DICTIONARY_FILE_2)
    >>> result = read_pronouncing_dictionary(dict_file_2)
    >>> result == EXPECTED_DICTIONARY_2
    True
    
    Precondition: The pronunciation file has the first line commented followed
    by every subsequent line starting with a capitalized word and followed by 
    capitalized phonemes of that word with every phoneme seperated by 
    a space and words seperated by new line characters
    """
    pronouncing_dictionary = {}
    for line in pronunciation_file.readlines():
        if not ";;;" in line and not line in '\n':
            components = line.split()
            first_element = components[0]
            components.remove(first_element)
            pronouncing_dictionary[first_element] = components
    return pronouncing_dictionary

def read_poetry_form_descriptions(
        poetry_forms_file: TextIO) -> POETRY_FORMS:
    """Return a dictionary of poetry form name to poetry pattern for the poetry
    forms in poetry_forms_file.
    >>> import io
    >>> form_file = io.StringIO(SAMPLE_POETRY_FORM_FILE)
    >>> result = read_poetry_form_descriptions(form_file)
    >>> result == EXPECTED_POETRY_FORMS
    True
    >>> import io
    >>> form_file_2 = io.StringIO(SAMPLE_POETRY_FORM_FILE_2)
    >>> result = read_poetry_form_descriptions(form_file_2)
    >>> result == EXPECTED_POETRY_FORMS_2
    True
    
    Precondition: The poetry form file must start with the name of the type of
    poem on line one, followed by each line composition which starts with a 
    number of syllables and ends with a rhyming scheme seperated by a space.
    Each poem form is seperated by a blank line.
    """
    
    poem_forms = {}
    line_number = 0
    key = ""
    poems = poetry_forms_file.readlines()
    a_poem_form = ()
    while line_number < len(poems):
        if poems[line_number].strip().isalpha():
            key = poems[line_number].strip()
            line_number += 1
        elif not poems[line_number].strip().isalpha() and poems[line_number] != "\n": 
            a_poem_form, line_number = read_a_poetry_form_description(poems, line_number)
            if line_number == len(poems):
                poem_forms[key] = a_poem_form
        else:
            poem_forms[key] = a_poem_form
            line_number += 1
    return poem_forms   

def read_a_poetry_form_description(
        poems: List[str], line_number: int) -> (Tuple[List[int], List[str]], int):
    """Return a list of the rhyme and syllabic pattern for a line of poetry.
    
    >>> read_a_poetry_form_description(['Limerick', '8 A', '8 A', '5 B', '5 B', '8 A', 'Haiku', '5 *', '7 *', '5 *'], 1)
    (([8, 8, 5, 5, 8], ['A', 'A', 'B', 'B', 'A']), 6)
    >>> read_a_poetry_form_description(['Limerick', '8 A', '8 A', '5 B', '5 B', '8 A', 'Haiku', '5 *', '7 *', '5 *'], 7)
    (([5, 7, 5], ['*', '*', '*']), 10)
    
    Precondition: The list of poem forms must follow the order indicated in above
    function, with each element including a newline character as a seperate element
    in the list. The line number must be less than the length of the list of poem
    forms.
    """
    
    rhyming_lst = []
    syllabic_lst = []
    while (line_number < len(poems) and not poems[line_number].strip().isalpha() and 
            poems[line_number] != "\n"): 
        components = poems[line_number].strip().split()
        components[0] = ((int)(components[0]))
        rhyming_lst.append(components[1])
        syllabic_lst.append(components[0])
        line_number += 1
    return (syllabic_lst, rhyming_lst), line_number


if __name__ == '__main__':
    import doctest

    doctest.testmod()

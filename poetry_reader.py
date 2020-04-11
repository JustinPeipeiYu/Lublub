"""Functions for reading the pronouncing dictionary and the poetry forms files
"""
from typing import TextIO
from typing import List


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

EXPECTED_POETRY_FORMS = {
    'Haiku': ([5, 7, 5], ['*', '*', '*']),
    'Limerick': ([8, 8, 5, 5, 8], ['A', 'A', 'B', 'B', 'A'])
}

SAMPLE_DICTIONARY_FILE = ''';;; Comment line
ABSINTHE  AE1 B S IH0 N TH
HEART  HH AA1 R T
FONDER  F AA1 N D ER0
'''

EXPECTED_DICTIONARY = {
    'ABSINTHE': ['AE1', 'B', 'S', 'IH0', 'N', 'TH'],
    'HEART': ['HH', 'AA1', 'R', 'T', ],
    'FONDER': ['F', 'AA1', 'N', 'D', 'ER0']
}

SAMPLE_POEM_FILE = '''  Is this mic on?

Get off my lawn.
'''


def read_and_trim_whitespace(poem_file: TextIO) -> str:
    """Return a string containing the poem in poem_file, with
    blank lines and leading and trailing whitespace removed.
    >>> import io
    >>> poem_file = io.StringIO(SAMPLE_POEM_FILE)
    >>> read_and_trim_whitespace(poem_file)
    'Is this mic on?\\n\\nGet off my lawn.'
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
    """
    pronouncing_dictionary = {}
    for line in pronunciation_file.readlines():
        if not ";;;" in line and not line in ['\n', '\t']:
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
    """
    
    poem_forms = {}
    rhyming_lst = []
    syllabic_lst = []
    key = ""
    poems = poetry_forms_file.readlines()
    for line in poems:
        if line != poems[-1]:
            if line.strip().isalpha():
                key = line.strip()
            elif not line.strip().isalpha() and not line in ["\n", "\t"]:    
                lst = read_poetry_form_description(line.strip())
                rhyming_lst.append(lst[1])
                syllabic_lst.append(lst[0])
            else:
                poem_forms[key] = (syllabic_lst, rhyming_lst)
                print(poem_forms)
                rhyming_lst = []
                syllabic_lst = []  
        else:
            lst = read_poetry_form_description(line.strip())
            rhyming_lst.append(lst[1])
            syllabic_lst.append(lst[0])
            poem_forms[key] = (syllabic_lst, rhyming_lst)
    return poem_forms   
    
def read_poetry_form_description( 
        line: str) -> List[str]:
    """Return a list of the rhyme and syllabic pattern for a line of poetry.
    
    >>> read_poetry_form_description("8 A")
    [8, 'A']
    """
    
    components = line.split()
    components[0] = ((int)(components[0]))
    return components

if __name__ == '__main__':
    import doctest

    doctest.testmod()
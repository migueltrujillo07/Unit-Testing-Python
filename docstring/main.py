# Docstring 
def palindromo (sentence: str) -> bool: 

    """Permite conocer si un string es, o no, un palindromo.

    Args:
        Sentence: String

    Returns:
        bool
    
    examples:
        >>> palindromo('Anita lava la tina')
        True

        >>> palindromo('CodigoFacilito')
        False

        >>> sentence = 'oso'
        >>> palindromo(sentence)
        False
    """

    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]

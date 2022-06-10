# Docstring 
def palindromo (sentence: str) -> bool: 

    """Permite conocer si un string es, o no, un palindromo.

    Args:
        Sentence: String

    Returns:
        bool
    """

    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]

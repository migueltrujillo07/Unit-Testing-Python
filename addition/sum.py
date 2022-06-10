def sum_positive_numbers (n1: int, n2: int) -> int:
    """It allows to sum tow integers numbers

    arg (int):
        n1 (int)
        n2 (int)

    returns:
        int
     if n1 < 0 or n2 < 0:
        return None
    """
    assert n1 > 0 and n2 > 0,'We sorry you just can sum positive integers'

    return n1 + n2
if __name__ == '__main__':
    result = sum_positive_numbers(-10 , 20)
    print(result)

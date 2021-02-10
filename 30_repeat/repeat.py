def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    # rpt_phrase = ""
    # times = 0
    # if isinstance(num, int):
    #     while times < num:
    #         times + 1
    #         rpt_phrase += phrase    
    # else:
    #     return None
    # return rpt_phrase
    if not isinstance(num, int) or num < 0:
        return None

    return phrase * num

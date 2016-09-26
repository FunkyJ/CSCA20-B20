def get_letter_grade(percentage):
    """
    (number) -> 'str'
    Return the letter grade for the given percentage grade.
    Assume that percentage is a value between 0 and 100.
    >>> get_letter_grade(20)
    'F'
    >>> get_letter_grade(65)
    'C'
    >>> get_letter_grade(52)
    'D'
    >>> get_letter_grade(80)
    'A'
    >>> get_letter_grade(76)
    'B'
    """
    if percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'


def get_plus_minus(percentage):
    """
    (number) -> str
    Return whether the given grade is in a '+', '-' or ''
    range for it's corresponding letter grade.
    Assume that percentage is a value between 0 and 100.
    >>> get_plus_minus(78)
    '+'
    >>> get_plus_minus(85)
    ''
    >>> get_plus_minus(90)
    '+'
    >>> get_plus_minus(61)
    '-'
    >>> get_plus_minus(44)
    ''
    """
    if percentage >= 80:
        if percentage >= 90:
            return '+'
        if percentage >= 85:
            return ''
        if percentage >= 80:
            return '-'
    elif percentage >= 70:
        if percentage >= 77:
            return '+'
        if percentage >= 73:
            return ''
        if percentage >= 70:
            return '-'
    elif percentage >= 60:
        if percentage >= 67:
            return '+'
        if percentage >= 63:
            return ''
        if percentage >= 60:
            return '-'
    elif percentage >= 50:
        if percentage >= 57:
            return '+'
        if percentage >= 53:
            return ''
        if percentage >= 50:
            return '-'
    else:
        return ''


def convert_percentage_to_letter(percentage):
    """
    (number) -> str
    Return the letter grade including '+', '-' for the given
    percentage grade as defined by the UTSC GPA guidelines.
    Assume that percentage is a value between 0 and 100.
    >>> convert_percentage_to_letter(46)
    'F'
    >>> convert_percentage_to_letter(58)
    'D+'
    >>> convert_percentage_to_letter(62)
    'C-'
    >>> convert_percentage_to_letter(74)
    'B'
    >>> convert_percentage_to_letter(87)
    'A'
    >>> convert_percentage_to_letter(95)
    'A+'
    """
    return (get_letter_grade(percentage) + get_plus_minus(percentage))

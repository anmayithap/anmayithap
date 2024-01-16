def to_roman(value: int) -> str:
    """Convert integer value to roman.

    Symbol       Value
    I            1
    V            5
    X            10
    L            50
    C            100
    D            500
    M            1000

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.
    """
    result: str = ''

    ranges: tuple[tuple[int, str], ...] = (
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    )

    for series, roman in ranges:
        integer: int = value // series
        value -= integer * series
        result += integer * roman

    return result


if __name__ == '__main__':
    assert to_roman(1994) == 'MCMXCIV'

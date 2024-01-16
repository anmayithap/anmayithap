def convert_to_zig_zag(string: str, rows: int) -> str:
    if rows == 1:
        return string

    matrix: list[list[str]] = [
        [] for _ in range(rows)
    ]

    row: int = 0
    reversed: bool = False

    for letter in string:
        matrix[row].append(letter)

        if row + 1 == rows:
            reversed = True
        elif row == 0:
            reversed = False

        if not reversed:
            row += 1
        else:
            row -= 1

    result: str = ''

    for string_row in matrix:
        pre_result: str = ''.join(string_row)
        result += pre_result

    return result


if __name__ == '__main__':
    assert convert_to_zig_zag('ABC', 1) == 'ABC'

import string


def is_palindrome(any_string: str) -> bool:
    access_chars: str = string.ascii_lowercase + string.digits
    forward: int = 0
    reverse: int = len(any_string) - 1
    result: bool = True

    while forward < reverse:
        to_continue: bool = False
        left, right = any_string[forward].lower(), any_string[reverse].lower()

        if left not in access_chars:
            forward += 1
            to_continue = True
        if right not in access_chars:
            reverse -= 1
            to_continue = True
        if to_continue:
            continue

        if left != right:
            result = False
            break
        else:
            forward += 1
            reverse -= 1

    return result


if __name__ == '__main__':
    print(is_palindrome('A0'))

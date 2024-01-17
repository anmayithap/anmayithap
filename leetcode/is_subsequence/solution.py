def is_subsequence(sub: str, target: str) -> bool:
    count: int = 0

    for letter in target:
        try:
            if letter == sub[count]:
                count += 1
        except IndexError:
            continue

    if count == len(sub):
        return True
    return False

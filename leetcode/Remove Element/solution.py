def remove_element(target: list[int], value: int) -> int:
    target.sort(key=lambda item: item == value)

    while target and target[-1] == value:
        target.pop(-1)

    return len(target)


if __name__ == '__main__':
    target: list[int] = [0, 1, 2, 2, 3, 0, 4, 2]
    count: int = remove_element(target, 2)

    assert count == 5

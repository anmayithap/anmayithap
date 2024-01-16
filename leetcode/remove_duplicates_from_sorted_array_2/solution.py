def remove_duplicates(target: list[int]) -> int:
    count: int = 2

    for idx in range(2, len(target)):
        if target[idx] > target[count - 2]:
            target[count] = target[idx]
            count += 1

    return count


if __name__ == '__main__':
    target: list[int] = [1, 1, 1, 2, 2, 3]

    count: int = remove_duplicates(target)

    assert count == 5

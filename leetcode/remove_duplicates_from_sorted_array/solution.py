def remove_duplicates(target: list[int]) -> int:
    target[:] = list(set(target))
    target.sort()

    return len(target)


if __name__ == '__main__':
    import random

    target: list[int] = [random.randint(0, 10) for _ in range(100)]

    count: int = remove_duplicates(target)

    assert len(set(target)) == count

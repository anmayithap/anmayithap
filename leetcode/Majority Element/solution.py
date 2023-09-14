from collections import Counter


def majority_element(target: list[int]) -> int:
    return Counter(target).most_common(1)[0][0]


if __name__ == '__main__':
    target: list[int] = [1, 1, 1, 2, 2, 1, 1, 1]
    item: int = majority_element(target)

    assert item == 1

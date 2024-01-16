def candy(ratings: list[int]) -> int:
    candy_count: int = 1
    left, right, target = 0, 0, 0

    for previous, current in zip(ratings[:-1], ratings[1:]):
        if previous < current:
            left, right, target = left + 1, 0, left + 1
            candy_count += 1 + left
        elif previous == current:
            left = right = target = 0
            candy_count += 1
        else:
            left, right = (0, right + 1)
            candy_count += 1 + right - int(target >= right)

    return candy_count

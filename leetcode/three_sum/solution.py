def get_three_sum(numbers: list[int]) -> list[tuple[int, ...]]:
    numbers.sort()

    result: list[tuple[int, ...]] = []

    for idx in range(len(numbers)):
        if idx > 0 and numbers[idx] == numbers[idx - 1]:
            continue

        target: int = -numbers[idx]

        left, right = idx + 1, len(numbers) - 1

        while left < right:
            temp: int = numbers[left] + numbers[right]

            if temp == target:
                triplet: tuple[int, ...] = (
                    numbers[idx],
                    numbers[left],
                    numbers[right],
                )
                result.append(triplet)
                left += 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
            elif temp > target:
                right -= 1
            else:
                left += 1

    return result


if __name__ == '__main__':
    numbers: list[int] = [-1, 0, 1, 2, -1, -4, 3]

    print(get_three_sum(numbers))

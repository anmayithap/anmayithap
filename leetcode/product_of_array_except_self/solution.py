def product_except_self(target: list[int]) -> list[int]:
    output: list[int] = [1 for _ in range(len(target))]

    for idx in range(1, len(target)):
        output[idx] = output[idx - 1] * target[idx - 1]

    reversed_operation: int = 1

    for idx in range(len(target) - 1, -1, -1):
        output[idx] *= reversed_operation
        reversed_operation *= target[idx]

    return output


if __name__ == '__main__':
    result: list[int] = product_except_self([1, 2, 3, 4])

    assert result == [24, 12, 8, 6]

def h_index(citations: list[int]) -> int:
    citations.sort(reverse=True)
    h_index: int = 0

    for idx, citation in enumerate(citations, start=1):
        if idx > citation:
            break
        else:
            h_index += 1
    return h_index


if __name__ == '__main__':
    target: list[int] = [3, 0, 6, 1, 5]
    result: int = h_index(target)

    assert result == 3

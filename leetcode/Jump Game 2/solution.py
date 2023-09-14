def jump(steps: list[int]) -> int:
    result: int = 0
    end: int = 0
    farthest: int = 0

    for idx, step in enumerate(steps[:-1]):
        farthest = max(farthest, idx + step)
        if farthest >= len(steps) - 1:
            result += 1
            break
        if idx == end:
            result += 1
            end = farthest
    return result

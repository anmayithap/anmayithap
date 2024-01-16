def rotate(target: list[int], shift: int) -> None:
    shift = shift % len(target)
    target[:] = target[-shift:] + target[:-shift]

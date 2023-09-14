def can_jump(steps: list[int]) -> bool:
    current_place = steps[0]

    for _, step in enumerate(steps[1:], start=1):
        if current_place == 0:
            return False
        current_place -= 1
        current_place = max(current_place, step)

    return True

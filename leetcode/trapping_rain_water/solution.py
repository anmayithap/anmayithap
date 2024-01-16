def trap(height: list[int]) -> int:
    left_ptr, right_ptr = 0, len(height) - 1
    max_left, max_right = height[left_ptr], height[right_ptr]
    water_volume: int = 0

    while left_ptr < right_ptr:
        if max_left < max_right:
            left_ptr += 1
            max_left = max(max_left, height[left_ptr])
            water_volume += max_left - height[left_ptr]
        else:
            right_ptr -= 1
            max_right = max(max_right, height[right_ptr])
            water_volume += max_right - height[right_ptr]

    return water_volume

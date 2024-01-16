def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    target_position: int = 0
    total: int = 0

    for i in range(len(gas)):
        total += gas[i] - cost[i]

        if total < 0:
            total = 0
            target_position = i + 1

    return target_position

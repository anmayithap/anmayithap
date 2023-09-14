def merge(
    master: list[int],
    master_size: int,
    target: list[int],
    target_size: int,
) -> None:
    idx: int = master_size

    for item in target[:target_size]:
        master[idx] = item
        idx += 1

    master.sort()


if __name__ == '__main__':
    master: list[int] = [1, 2, 3, 0, 0, 0]
    target: list[int] = [2, 5, 6]

    merge(
        master=master,
        master_size=3,
        target=target,
        target_size=3,
    )

    assert master == [1, 2, 2, 3, 5, 6]

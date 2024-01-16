import random


class RandomizedSet:
    __slots__: tuple[str, ...] = (
        '_hashmap',
        '_indexes',
    )

    def __init__(self) -> None:
        self._hashmap: dict[int, int] = {}
        self._indexes: list[int] = []

    def insert(self, value: int) -> bool:
        result: bool = False
        if value not in self._hashmap:
            self._hashmap[value] = len(self._indexes)
            self._indexes.append(value)
            result = True
        return result

    def remove(self, value: int) -> bool:
        result: bool = False
        if value in self._hashmap:
            self._indexes.remove(value)
            self._hashmap.pop(value)
            result = True
        return result

    def get_random(self) -> int:
        return random.choice(self._indexes)

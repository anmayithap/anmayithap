def get_longest_common_prefix(words: list[str]) -> str:
    if len(words) == 1:
        return words[0]

    words.sort(key=lambda item: len(item))
    shortest_word: str = words[0]
    mask: list[int | None] = [None for _ in range(len(shortest_word))]

    for idx in range(1, len(words)):
        for letter_idx in range(len(shortest_word)):
            if mask[letter_idx] == 0:
                break
            mask[letter_idx] = 1 if words[idx][letter_idx] == shortest_word[letter_idx] else 0

    prefix = ''

    for idx in range(len(mask)):
        if not mask[idx]:
            break
        prefix += shortest_word[idx]

    return prefix


if __name__ == '__main__':
    target: list[str] = ["abab", "aba", "abc"]
    assert get_longest_common_prefix(target) == 'ab'

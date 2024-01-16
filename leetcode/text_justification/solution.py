def justify(words: list[str], max_width: int) -> list[str]:
    justify_words: list[list[str]] = []
    result: list[str] = []

    access_words: list[str] = []
    current_width: int = 0

    for word in words:
        temp_width: int = current_width
        if not access_words:
            temp_width += len(word)
        else:
            temp_width += len(word) + 1

        if temp_width > max_width:
            if current_width < max_width and len(access_words) == 1:
                access_words.append(' ' * (max_width - current_width))
            elif current_width < max_width:
                spaces: int = (len(access_words) - 1) // 2
                remaining_width: int = max_width - current_width
                if remaining_width % spaces != 0:
                    i: int = 0
                    while remaining_width:
                        if access_words[i][0] == ' ':
                            access_words[i] += ' '
                            remaining_width -= 1
                        if i + 1 == len(access_words):
                            i = 0
                        else:
                            i += 1
                else:
                    to_add: int = remaining_width // spaces
                    for i in range(len(access_words)):
                        if access_words[i] == ' ':
                            access_words[i] += ' ' * to_add
            justify_words.append(access_words)
            access_words = [word]
            current_width = len(word)
        else:
            if access_words:
                access_words.append(' ')
            access_words.append(word)
            current_width = temp_width

    if access_words:
        access_words.append(' ' * (max_width - current_width))
        justify_words.append(access_words)

    for idx in range(len(justify_words)):
        result.append(''.join(justify_words[idx]))

    print(result)

    return result


if '__main__' == __name__:
    words: list[str] = ["The", "important", "thing", "is", "not", "to", "stop",
                        "questioning.", "Curiosity", "has", "its", "own", "reason", "for", "existing."]
    justify(words, max_width=17)

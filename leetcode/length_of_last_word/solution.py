def get_len_of_last_word(text: str) -> int:
    counter: int = 0

    for i in range(len(text) - 1, -1, -1):
        if text[i] == ' ' and not counter:
            continue
        elif text[i] == ' ' and counter:
            break
        else:
            counter += 1

    return counter

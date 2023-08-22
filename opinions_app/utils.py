from random import choices

ASCII_SYMBOLS = (*range(48, 58), *range(65, 91), *range(97, 123))


def random_href():
    return ''.join(map(chr, choices(ASCII_SYMBOLS, k=6)))

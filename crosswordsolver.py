def solve(grid, words, is_diagonal = True):
    DIRECTIONS_DIAGONAL = [
        (1, 0),
        (0, 1),

        (-1, 1),
        (1, 1)
    ]

    DIRECTIONS_ADJACENT = [
        (1, 0),
        (0, 1),
    ]

    directions = DIRECTIONS_DIAGONAL if is_diagonal else DIRECTIONS_ADJACENT

    for word in words.copy():
        words.append(''.join(reversed(word)))

    len_max_word = len(max(words))
    matches = []

    for at in grid:
        for direction in directions:
            match = grid.walk_sum(at, direction, len_max_word)
            
            for word in words:
                if match.startswith(word):
                    matches.append((
                        word,
                        at,
                        direction,
                    ))

    return matches
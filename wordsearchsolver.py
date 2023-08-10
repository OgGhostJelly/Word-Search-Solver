from gridtools import add_v2_v2
from gridtools import mult_v2_i
from gridtools import walk_dist

from trietools import list_to_trie
from trietools import match

from colorama import Fore, Style


# Looks at a tile facing a direction in a grid and checks if a word is placed there.

def look_for(grid, words, at, direction):
    def step():
        nonlocal at
        nonlocal grid

        while at in grid:
            yield grid[at]
            at = add_v2_v2(at, direction)

    return match(words, step())


# Solves a crossword puzzle and returns its solutions in a tuple with this format:
# ( word, at, direction )

def solve(grid, _words, is_diagonal = True):
    # get directions

    directions = [
        (1, 0),
        (0, 1),

        (-1, 1),
        (1, 1)
    ] if is_diagonal else [
        (1, 0),
        (0, 1),
    ]


    # prepare words

    words = []
    
    for word in _words:
        words.append(word)
        words.append(''.join(reversed(word)))
    
    words = list_to_trie(words)
    

    # search

    matches = []

    for at in grid:
        if not grid[at] in words:
            continue

        for direction in directions:
            match = look_for(grid, words, at, direction)

            if match:
                matches.append((
                    match,
                    at,
                    direction,
                ))
    
    return matches


# Converts a grid and a crossword solution to a string, used for debugging.

def sol2str(grid, sol):
    solved_cells = {}

    for at, _ in walk_dist(grid, sol[1], sol[2], len(sol[0])):
        solved_cells[at] = None


    y = None
    string = ""

    for at in grid:
        if y != at[1]: y = at[1]; string += "\n"
        string += (
            Fore.YELLOW + grid[at] + Style.RESET_ALL
            if at in solved_cells else
            grid[at]
        )
    
    string = f"{sol[0]}|{''.join(reversed(sol[0]))} at {sol[1]} + {mult_v2_i(sol[2], len(sol[0])-1)}\n---\n" + string[1:]

    return string
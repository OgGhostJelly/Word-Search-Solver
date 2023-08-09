from gridtools import add_v2_v2
from gridtools import mult_v2_i
from gridtools import walk_ats

from trietools import strlist_to_trie

from colorama import Fore, Style


# Casts a ray and checks for the existance of a word in the given words trie
# If no word is found return None

def look_for(grid, words, at, direction):
    if not grid[at] in words:
        return

    shifted_at = add_v2_v2(at, direction)

    if not shifted_at in grid:
        return
    
    if words[grid[at]] is True:
        return grid[at]
    
    data = look_for(grid, words[grid[at]], shifted_at, direction)
    return grid[at] + data if data else None


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
    
    words = strlist_to_trie(words)
    

    # search

    matches = []

    for at in grid:
        for direction in directions:
            match = look_for(grid, words, at, direction)

            if match:
                matches.append((
                    match,
                    at,
                    direction,
                ))
    
    return matches


# Converts a grid and a crossword solution to a string.

def sol2str(grid, sol):
    solved_cells = {}

    for at in walk_ats(grid, sol[1], sol[2], len(sol[0])):
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
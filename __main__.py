from gridtools import grid_from_iterable

from wordsearchsolver import sol2str
from wordsearchsolver import solve


if __name__ == "__main__":
    crossword_str, words_str = open("crossword.txt", "r").read().split('-', 1)

    grid = grid_from_iterable(crossword_str)
    words = words_str.split("\n")
    
    for sol in solve(grid, words):
        print(sol2str(grid, sol), end='\n\n')
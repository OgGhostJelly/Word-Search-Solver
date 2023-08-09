from gridtools import Grid
from crosswordsolver import solve
from colorama import Fore, Style


def mult_v2_i(a, b):
    return (a[0] * b, a[1] * b)


def sol2str(grid, sol):
    solved_cells = {}
    for at in grid.walk(sol[1], sol[2], len(sol[0])-2):
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
    
    string = string[1:]

    return string


if __name__ == "__main__":
    crossword_str = open("crossword.txt", "r").read()
    words_str = open("words.txt", "r").read()

    grid = Grid.from_iterable(crossword_str)
    words = words_str.split("\n")

    solutions = solve(grid, words)


    for sol in solutions:
        print(f"{sol[0]}|{''.join(reversed(sol[0]))} at {sol[1]} + {mult_v2_i(sol[2], len(sol[0])-1)}")
        print("---")
        print(sol2str(grid, sol))
        print()
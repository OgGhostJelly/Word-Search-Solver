def grid_from_iterable(iterable, newline_val = "\n"):
    x = 0
    y = 0
    _cells = {}

    for val in iterable:
        if val == newline_val:
            y += 1
            x = 0
            continue
        
        _cells[(x, y)] = val
        x += 1
    
    return _cells


def add_v2_v2(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mult_v2_i(a, b):
    return (a[0] * b, a[1] * b)


def walk(grid, at, direction):
    i = 0
    while at in grid:
        yield at, i
        at = add_v2_v2(at, direction)
        i += 1


def walk_dist(grid, at, direction, distance):
    walk_gen = walk(grid, at, direction)
    for at, i in walk_gen:
        yield at, i
        if i >= distance - 1:
            walk_gen.close()
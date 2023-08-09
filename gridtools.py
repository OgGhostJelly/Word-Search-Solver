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


def walk(grid, at, direction, key, should_continue):
    if not at in grid:
        return
    
    if not should_continue(at):
        return

    key(at)
    walk(grid, add_v2_v2(at, direction), direction, key, should_continue)


def walk_ats(grid, at, direction, distance):
    ats = []
    depth = 0

    def key(at):
        nonlocal depth

        ats.append(at)
        depth += 1

    def should_continue(_):
        return depth < distance
    
    walk(grid, at, direction, key, should_continue)

    return ats
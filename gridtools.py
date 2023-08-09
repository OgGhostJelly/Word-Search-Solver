def add_v2_v2(a, b):
    return (a[0] + b[0], a[1] + b[1])


class Grid:
    @staticmethod
    def from_iterable(iterable, newline_val = "\n"):
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
        
        return Grid(_cells)
    

    # Moves from a starting position facing a direction, and concats the values of the _cells it lands on.
    # How the method concatenates can be customized using the key parameter.
    # Stops when hitting an empty cell or surpassed dist.
    def walk_sum(self, at, dir, dist, key = lambda a, b: a + b):
        return self.walk(at, dir, dist, lambda s, a, b: key(s[a], b), lambda s, x: s[x])
    

    def walk(self, at, dir, dist, key = lambda _, a, b: [a, *b], leaf = lambda _, x: (x,)):
        if dist < 0:
            return leaf(self, at)
        
        shifted_at = add_v2_v2(at, dir)

        if not shifted_at in self._cells:
            return leaf(self, at)

        data = self.walk(shifted_at, dir, dist - 1, key, leaf)
        return key(self, at, data)


    def __init__(self, cells):
        self._cells = cells
    
    def __str__(self) -> str:
        return str(self._cells)

    def __len__(self):
        return len(self._cells)
    
    def __iter__(self):
        yield from self._cells
    
    def __getitem__(self, key):
        return self._cells[key]
import itertools

s3 = sqrt(3)
s32 = sqrt(3) / 2
s34 = sqrt(3) / 4

def _BFS_sierp(base, x, y, pilot):
    triangle(x + base[1], y,
             x + base[2], y + base[4],
             x + base[3], y + base[4])

    yield
    
    if pilot:
        base[:] = [i * 0.5 for i in base]

    children = [_BFS_sierp(base, x, y, pilot),
                _BFS_sierp(base, x + base[0], y, False),
                _BFS_sierp(base, x + base[1], y + base[5], False)]

    for i in itertools.cycle(children):
        yield next(i)

def BFS_sierp(base, x, y):
    return _BFS_sierp([base, base * 0.5, base * 0.25, base * 0.75, base * s34, base * s32], x, y, True)
from sierp import BFS_sierp, s32

def setup():
    global si
    size(800, 800)
    background(255)
    fill(0)
    triangle(50, 50,
             750, 50,
             400, 50 + 700 * s32)
    noStroke()
    fill(255)
    si = BFS_sierp(700, 50, 50)

def draw():
    next(si)

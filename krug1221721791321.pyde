a = 0

def setup():
    size(600,600)
    fill(1)
def draw():
    global a
    background(250)
    ellipse(300,300,a,a)
    if keyPressed:
        global a
        if key == CODED:
            if keyCode == UP: 
                a = a + 1
            elif keyCode == DOWN:
                a = a - 1
                if a == 0:
                    a = 1

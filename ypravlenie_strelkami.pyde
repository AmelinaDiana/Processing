a = 300
b = 300

def setup():
    size(600,600)
    frameRate(100)
    
def draw():
    background(250)
    ellipse(b,a,100,100)
def keyPressed():
    global a,b
    if key == CODED:
        if keyCode == UP:
            a = a - 1
        if keyCode == DOWN:
            a = a + 1
        if keyCode == LEFT:
            b = b - 1
        if keyCode == RIGHT:
            b = b + 1
            

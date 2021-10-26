x = 0
def setup():
    size(600,600)
def draw():
    background(150)
    global x
    ellipse(x,x,50,50)
    x = x + 1

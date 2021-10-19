x = 20
def setup():
    size(600,600)
    
def draw():
    global x
    ellipse(x,x,x,x)
    x = x + 1    

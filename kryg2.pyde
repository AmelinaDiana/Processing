x = 900
def setup():
    size(600,600)
    
def draw():
    global x
    stroke(random(1,250))
    ellipse(300,300,x,x)
    x = x - 1    

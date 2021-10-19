x = 300
z = 300
def setup():
    size(600,600)
    
def draw():
    global x
    global z
    ellipse(z,x,50,50)
    ellipse(x,z,50,50)
    ellipse(x,x,50,50)
    ellipse(z,z,50,50)

    x = x + 1 
    z = z - 1   

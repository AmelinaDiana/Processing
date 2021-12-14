x = 300
y = 150

def setup():
    size(600,600)
    strokeWeight(5)
    
def draw(): 
    global x
    global y
    background(100)
    translate(x,y)
    ellipse(0,0,50,50)
    ellipse(0,63,75,75)
    ellipse(0,150,100,100)   
    point(-10,-5)
    point(10,-5)
    point(0,50)
    point(0,75)
    point(0,125)
    point(0,150)
    point(0,175)
    if mousePressed == True:
        x = mouseX
        y = mouseY
        
    
    
    

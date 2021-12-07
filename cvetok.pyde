angle = 0

def setup():
    size(600,400)
    frameRate(3)
def draw():
    global angle
    background(100)
    frameRate(25)  
    fill(random(250),random(250),random(250))
    translate(300,200)
    ellipse(0,0,20,20)
    rotate(radians(angle))
    ellipse(60,0,90,50)
    rotate(radians(30))
    ellipse(60,0,90,50)
    rotate(radians(30))
    ellipse(60,0,90,50)
    rotate(radians(30))
    ellipse(60,0,90,50)
    rotate(radians(30))
    ellipse(60,0,90,50)
    rotate(radians(30))
    ellipse(60,0,90,50)
    rotate(radians(30))
    ellipse(60,0,90,50)
    rotate(radians(30))
    ellipse(60,0,90,50)
    rotate(radians(30))
    ellipse(60,0,90,50)
    rotate(radians(30))
    ellipse(60,0,90,50)
    rotate(radians(30))
    ellipse(60,0,90,50)
    rotate(radians(30))
    ellipse(60,0,90,50)
    
    angle = angle + 1

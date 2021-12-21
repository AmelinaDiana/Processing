def setup():
    size(600,600)
    background(100)
    strokeWeight(7)
    fill(250)
def draw(): 
    if mousePressed == True and mouseButton == RIGHT:
        noLoop
        stroke(255, 100, 0)
        fill(255, 100, 0)
        ellipse(300,300,150,120)
        stroke(1)
        fill(1)
        triangle(275,270,285,290,265,290)
        triangle(330,270,340,290,320,290)
        triangle(275,320,285,320,330,320)
        stroke(250)
        fill(250)

    if mousePressed == True and mouseButton == LEFT:
        noLoop
        stroke(250)
        ellipse(100,100,100,100)
        triangle(100,151,151,100,170,170)
        triangle(150,160,170,170,168,198)
        stroke(1)
        ellipse(115,115,25,25)
        point(80,100)
        point(100,80)
    
    if mousePressed == False:
        background(100)

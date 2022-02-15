bg = 250;
sw = 5
def setup():
    global bg
    global sw
    textSize(12)
    size(600,600)
    background(250)
    strokeWeight(sw)
    frameRate(100)    
def draw():
    global bg
    global sw
    fill(1)
    if mousePressed == True:
        global sw
        global bg
        line(mouseX,mouseY,mouseX,mouseY)
        if mouseX > 25 and mouseX < 100 and mouseY > 75 and mouseY < 125:
            background = 250
        if mouseX > 125 and mouseX < 200 and mouseY > 25 and mouseY < 125:
            sw = sw + 1 
        if mouseX > 225 and mouseX < 300 and mouseY > 25 and mouseY < 125:
            sw = sw - 1 
            
    else:
        bg = 250

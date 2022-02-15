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
    text(u"Стереть",37,100)
    text(u"Линия толще",123,100)
    text(u"Линия тоньше",223,100)
    rect(25,25,75,50)
    rect(125,25,75,50)
    rect(225,25,75,50)
     
    if mousePressed == True:

        line(mouseX,mouseY,mouseX,mouseY)
        if mouseX > 25 and mouseX < 100 and mouseY > 25 and mouseY < 75:
            background(250)
        if mouseX > 125 and mouseX < 200 and mouseY > 25 and mouseY < 125:
            sw = sw + 1 
        if mouseX > 225 and mouseX < 300 and mouseY > 25 and mouseY < 125:
            sw = sw - 1 
            
    else:
        bg = 250

bg = 250;
sw = 5
def setup():
    global bg
    global sw
    textSize(12)
    size(800,800)
    background(250)
    strokeWeight(sw)
    frameRate(100)    
def draw():
    global bg
    global sw
    strokeWeight(5)
    fill(1)
    text(u"Стереть",25,70)
    text(u"Линия толще",110,70)
    text(u"Линия тоньше",210,70)
    rect(25,25,50,25)
    rect(125,25,50,25)
    rect(225,25,50,25)
    fill(50,205,50)
    rect(325,25,50,25)
     
    if mousePressed == True:
        strokeWeight(sw)
        line(pmouseX,pmouseY,mouseX,mouseY)
        if mouseX > 25 and mouseX < 75 and mouseY > 25 and mouseY < 50:
            background(250)
        if mouseX > 125 and mouseX < 175 and mouseY > 25 and mouseY < 50:
            sw = sw + 1 
        if mouseX > 225 and mouseX < 275 and mouseY > 25 and mouseY < 50:
            sw = sw - 1 
            if sw == 0:
                sw = 1
 
    else:
        bg = 250

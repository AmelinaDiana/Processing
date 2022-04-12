x = 0
y = 0
z = 0
bg = 250;
sw = 5
def setup():
    global x
    global y
    global z
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
    global x
    global y
    global z
    fill(1)
    strokeWeight(3)
    text(u"Стереть",25,70)
    text(u"Линия толще",110,70)
    text(u"Линия тоньше",210,70)
    stroke(0)
    rect(25,25,50,25)
    stroke(0)
    rect(125,25,50,25)
    stroke(0)
    rect(225,25,50,25)
    fill(50,205,50)
    stroke(0)
    rect(300,25,50,25)
    fill(255,0,0)
    stroke(0)
    rect(375,25,50,25)
    fill(255,255,0)
    stroke(0)
    rect(450,25,50,25)
    fill(0,0,255)
    stroke(0)
    rect(525,25,50,25)
    fill(255,255,255)
    stroke(0)
    rect(600,25,50,25)
    fill(1,1,1)
    stroke(0)
    rect(675,25,50,25)
    fill(1,1,1)
     
    if mousePressed == True:
        stroke(x,y,z)
        strokeWeight(sw)
        line(pmouseX,pmouseY,mouseX,mouseY)
def mouseClicked():
        global x
        global y
        global z
        global sw
        if mouseX > 25 and mouseX < 75 and mouseY > 25 and mouseY < 50:
            background(250)
        if mouseX > 125 and mouseX < 175 and mouseY > 25 and mouseY < 50:
            sw = sw + 1 
        if mouseX > 225 and mouseX < 275 and mouseY > 25 and mouseY < 50:
            sw = sw - 1 
            if sw == 0:
                sw = 1
        if mouseX > 300 and mouseX < 350 and mouseY > 25 and mouseY < 50:  
            x = 0
            y = 255
            z = 0
        
        if mouseX > 450 and mouseX < 500 and mouseY > 25 and mouseY < 50:  
            x = 255
            y = 255
            z = 0
        
        if mouseX > 375 and mouseX < 425 and mouseY > 25 and mouseY < 50:  
            x = 255
            y = 0
            z = 0
        
        if mouseX > 525 and mouseX < 575 and mouseY > 25 and mouseY < 50:  
            x = 0
            y = 0
            z = 255
        
        if mouseX > 600 and mouseX < 650 and mouseY > 25 and mouseY < 50:  
            x = 250
            y = 250
            z = 250
        
        if mouseX > 675 and mouseX < 725 and mouseY > 25 and mouseY < 50:  
            x = 0
            y = 0
            z = 0
        
          

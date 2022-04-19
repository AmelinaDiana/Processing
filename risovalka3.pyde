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
    background(250)
    strokeWeight(sw)
    size(800,800)

def draw():
    global bg
    global sw
    global x
    global y
    global z
    fill(1)
    if mousePressed == True:
        stroke(x,y,z)
        strokeWeight(sw)
        line(pmouseX,pmouseY,mouseX,mouseY)
    if keyPressed:
        if key == "1":
            background(250)
        if key == "2":    
            sw = sw + 1
        if key == "3": 
            sw = sw - 1
            if sw == 0:
                sw = 1
        if key == "4":
            x = 0
            y = 255
            z = 0
        if key == "5":
            x = 255
            y = 255
            z = 0
        if key == "6":
            x = 255
            y = 0
            z = 0
        if key == "7":
            x = 0
            y = 0
            z = 255
        if key == "8":
            x = 250
            y = 250
            z = 250
        if key == "9":
            x = 0
            y = 0
            z = 0

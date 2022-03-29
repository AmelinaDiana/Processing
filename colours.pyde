a = 0
b = 0
c = 0
def setup():
    size(600,600)
    background(250)
    frameRate(1)
def draw():
    global a,b,c
    fill(a,b,c)
    rect(random(0,600),random(0,600), random(0,100),random(0,100))
    if keyPressed:
        if key == '1':
            a = 0
            b = 250
            c = 0
        if key == '2':
            a = 250
            b = 250
            c = 0
        if key == '3':
            a = 250
            b = 0
            c = 0
        if key == '4':
            a = 0
            b = 0
            c = 250
        if key == '5':
            a = 128
            b = 0
            c = 128
        if key == '6':
            a = 0
            b = 250
            c = 250
        if key == '7':
            a = 255
            b = 165
            c = 0 
            
    

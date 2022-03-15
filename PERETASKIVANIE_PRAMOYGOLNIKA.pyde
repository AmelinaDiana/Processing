a = 250
b = 250

def setup():
    rectMode(CENTER)
    frameRate(100)
    size(600,600)
def draw():
    global a, b
    background(250)
    rect(a,b,100,100)

    
    if mousePressed == True:
       if mouseX > a - 50 and mouseX < a + 50 and mouseY > b - 50 and mouseY < b + 50:
            a = mouseX
            b = mouseY

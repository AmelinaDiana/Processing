myText = 0

def setup():
    size(600,600)
    textSize(50)
    background(250)
    fill(1)
def draw():
    text(myText,300,300)
    if keyPressed:
        myText = myText + key
    else:
        background(250)

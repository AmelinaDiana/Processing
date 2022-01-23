a = 0
def setup():
    size(600,600)
    
def draw():
    global a
    background(255)
    fill(0)
    rect(230,100,150,100)
    textSize(60)
    text(a,280,300)
    noFill()
    
def mouseClicked():
    global a  
    if mouseX > 230 and mouseX < 380 and mouseY > 100 and mouseY < 200:
        a = a + 1

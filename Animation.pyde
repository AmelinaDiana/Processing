a = 0
b = 0
c = 0
def setup():
    size(600,600)
    background(250)   
    textSize(15)
    frameRate(5)
def draw():
    global a,b,c
    fill(1)
    text(u"Смена цвета",25,100)
    text(u"Очистить",165,100)
    rect(150,25,100,50)
    rect(25,25,100,50)
    fill(a,b,c)
    ellipse(random(0,600),random(150,600),random(0,100),random(0,100))

def mouseClicked():
    global a,b,c
    if mouseX > 25 and mouseX < 125 and mouseY > 25 and mouseY < 75:
        a = random(1,250)
        b = random(1,250)
        c = random(1,250)
    if mouseX > 150 and mouseX < 250 and mouseY > 25 and mouseY < 75: 
        background(250)   

a = 60
b = 60

def setup():
    size(600,600)


def draw():
    background(250)
    strokeWeight(3)
    ellipse(b,a,25,25)
    strokeWeight(5)
    line(0,120,60,120)
    line(120,0,120,60)

def keyPressed():
    global a,b
    if key == 'a' or key == u'ф':
        b = b - 2
    if key == 'd' or key == u'в':
        b = b + 2
    if key == 's' or key == u'ы':
        a = a + 2
    if key == 'w' or key == u'ц':
        a = a - 2
    if key == 'q' or key == u'й':
        a = a - 2
        b = b - 2
    if key == 'x' or key == u'ч':
        a = a + 2
        b = b + 2
    if key == 'z' or key == u'я':
        a = a + 2
        b = b - 2
    if key == 'e' or key == u'у':
        a = a - 2
        b = b + 2
        
    if key == CODED:
        if keyCode == UP:
            a = a - 2
        if keyCode == DOWN:
            a = a + 2
        if keyCode == LEFT:
            b = b - 2
        if keyCode == RIGHT:
            b = b + 2

    

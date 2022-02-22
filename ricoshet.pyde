x = 0
mode = "вправо"

def setup():
    size(600,600)
    frameRate(3)
def draw():
    global x,mode 
    background(250)
    ellipse(300,x,50,50)
    if mode == "вправо":
        x = x + 2
    if mode == "влево":
            x = x - 2
    if x >= 600:
        mode = "влево"
    if x <= 0:
        mode = "вправо"
        
            
    

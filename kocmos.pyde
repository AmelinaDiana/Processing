
def setup():
    size(800,800)
    background(25,25,112)
    frameRate(100)
   
def draw():
    frameRate(3)
    strokeWeight(random(1,5))
    stroke(255) 
    point(random(0,800),random(0,800))
    stroke(1) 
    strokeWeight(3)
    fill(255,215,0)
    ellipse(50,50,150,150)
    fill(30,144,255)
    ellipse(700,150,150,150)
    fill(0,128,0)
    ellipse(710,115,25,15)
    ellipse(670,160,15,25)
    ellipse(730,180,15,10)
    fill(250)
    ellipse(740,135,15,25)
    ellipse(690,195,25,15)
    fill(139,69, 19)
    ellipse(670,105,25,15)
    ellipse(700,150,15,15)
    fill(250)
    rect(100,250,120,340)
    fill(230, 0, 0)
    triangle(100,250,160,180,220,250) 
    triangle(120,560,60,670,100,700) 
    triangle(160,560,140,700,180,700)
    triangle(200,560,220,700,260,670)
    fill(30,144,255)
    ellipse(160,290,40,40)
    ellipse(160,340,40,40)
    ellipse(160,390,40,40)
    fill(1)
    rect(125,440,70,150) 
    
    if mousePressed:
        if mouseX > 125 and mouseX < 195 and mouseY > 440 and mouseY < 590:
            
            strokeWeight(3)
            stroke(1) 
            ellipse(400,400,50,150)    
            ellipse(400,300,70,70)
            translate(370,500)
            rotate(radians(25))
            ellipse(0,0,25,120)
            ellipse(-55,-100,20,100)
            rotate(radians(130))
            ellipse(-55,-30,25,100)
            ellipse(-110,75,20,100)

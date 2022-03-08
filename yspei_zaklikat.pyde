a = 0
def setup():
   size(600,600)
   textSize(30)
   frameRate(60)
  
def draw():
   global a
   textAlign(CENTER,CENTER)
   background(250)
   fill(1)
   text(u"очки:",255,240)
   text(a,315,240)
   rect(215,150,100,50)
   if a >= 30 and frameCount <= 30*60:
       background(250)
       text(u"Вы победили!",270,250)
   if a < 30 and frameCount > 30*60:
       background(250)
       text(u"Вы проиграли!",270,250)
       

def mouseClicked():
   global a  
   if mouseX > 215 and mouseX < 315 and mouseY > 150 and mouseY < 200:
       a = a + 1   

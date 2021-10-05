def setup():
   size(600,600)
   background(5)
   frameRate(1)
   
def draw():
    
   strokeWeight(random(1,5))
   stroke(random(200,255))
   point(random(0,600),random(0,600))

from graphics import *
import math
import random
def main():
    win = GraphWin("My Window",500,500)
    win.setCoords(0,200,200,0)
#    win.setBackground( 'blue' )
    i=int(input("enter color, 0 for red, 1 for green"))
    if( i==0):
        win.setBackground( color_rgb(255,0,0 ))
    else:
        win.setBackground( color_rgb(0,255,0 ))
    colval = []
    pt1 = Point(75,115)
    pt2 = Point(115,73)
    rec=Rectangle(pt1,pt2)
    rec.setFill(color_rgb(133,0,208 ))
    rec.draw(win)

# Shade interior of this robotic component
    nlev = 0
    for i in range(0,512):
    
      nlev = nlev +1
      if(nlev <128):
        a = 255
        b = (nlev-1)
        c = (nlev-1)
      elif (nlev>=128  and nlev < 384):
        a = (nlev-128)
        b = 255
        c = 255
      else:
        a = 0
        b = (128 + nlev-384)
        c = (128 + nlev-384)
      red = a
      green = b
      blue = c 
     
      colval.append( red + green *256 + blue *(256**2))
    for gg in range(1,201):
       hh = (gg-1)/200*(115-73)
       pt1 = Point(75+hh,115-hh)
       pt2 = Point(115-hh,73 +hh)
       
       rec= Rectangle( pt1,pt2)
        
       ind = int(hh/(115-73)*len(colval)) -1
#       if(gg == 50):
#        print(ind)
       color = colval[ind]
       red = color % 256
       col1 = int((color-red)/256)
       green = col1 %256
       blue = int((col1 - green)/256)
       red = int(red)
       blue = int(blue)
       green = int(green)
       if(gg == 50):
        print(red,green,blue)
       cond1 = (red>=0 and red<256)
       cond2 = (green>=0 and green<256)
       cond3 = (blue>=0 and blue<256)
       if(cond1 and cond2 and cond3):
       
         rec.setOutline(color_rgb(red,green,blue) )
       rec.draw(win)
        



#Arms 

    pt1 = Point(68,115)
    pt2 = Point(73,93)
    rec=Rectangle(pt1,pt2)
    rec.setFill(color_rgb(133,0,208 ))
    rec.draw(win)

    pt1 = Point(117,115)
    pt2 = Point(122,93)
    rec=Rectangle(pt1,pt2)
    rec.setFill(color_rgb(133,0,208 ))
    rec.draw(win)

# Legs

    pt1 = Point(85,135)
    pt2 = Point(95,117)
    rec=Rectangle(pt1,pt2)
    rec.setFill(color_rgb(133,0,208 ))
    rec.draw(win)

    pt1 = Point(97,135)
    pt2 = Point(107,117)
    rec=Rectangle(pt1,pt2)
    rec.setFill(color_rgb(133,0,208 ))
    rec.draw(win)

    pt1 = Point(83,98)  
    pt2 = Point(108,92)  
    rec=Rectangle(pt1,pt2)
    rec.setFill(color_rgb(250,250,250 ))
    rec.draw(win)

    pt1 = Point(87,70)
    pt2 = Point(77,53)
    rec=Rectangle(pt1,pt2)
    rec.setFill(color_rgb(133,0,208 ))
    rec.draw(win)

    pt1 = Point(112,70)
    pt2 = Point(102,53)
    rec=Rectangle(pt1,pt2)
    rec.setFill(color_rgb(133,0,208 ))
    rec.draw(win)
    
# components of snowman




# draw circle2
    pt= Point(90,80)
    cir = Circle(pt,3)
    cir.setFill(color_rgb(255,0,0 ))
    cir.draw(win)

    pt= Point(100,80)
    cir = Circle(pt,3)
    cir.setFill(color_rgb(255,0,0 ))
    cir.draw(win)

    win.getMouse()
    win.close()

main()
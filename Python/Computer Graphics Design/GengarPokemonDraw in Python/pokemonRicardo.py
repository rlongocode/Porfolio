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

    pt1 = Point(75,115)
    pt2 = Point(115,73)
    rec=Rectangle(pt1,pt2)
    rec.setFill(color_rgb(133,0,208 ))
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

#Ears

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
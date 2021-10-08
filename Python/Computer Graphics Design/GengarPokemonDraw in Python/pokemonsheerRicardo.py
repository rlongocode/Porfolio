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
    pt2 = Point(105, 115)
    pt3 = Point(115, 73)
    pt4 = Point(85, 73)
    poly1=Polygon(pt1,pt2,pt3,pt4)
    poly1.setFill(color_rgb(133,0,208 ))
    poly1.draw(win)

    pt1 = Point(63,95)
    pt2 = Point(93, 95)
    pt3 = Point(73, 73)
    pt4 = Point(43, 73)
    poly1=Polygon(pt1,pt2,pt3,pt4)
    poly1.setFill(color_rgb(133,0,208 ))
    poly1.draw(win)

    pt1 = Point(117,95)
    pt2 = Point(147,65)
    pt3 = Point(127,73)
    pt4 = Point(97,73)
    poly1=Polygon(pt1,pt2,pt3,pt4)
    poly1.setFill(color_rgb(133,0,208 ))
    poly1.draw(win)


    pt1 = Point(85,135)
    pt2 = Point(115,135)
    pt3 = Point(95, 117)
    pt4 = Point(65, 117)
    rec=Polygon(pt1,pt2,pt3,pt4)
    rec.setFill(color_rgb(133,0,208 ))
    rec.draw(win)

    pt1 = Point(97,135)
    pt2 = Point(127,135)
    pt3 = Point(107,117)
    pt4= Point(77, 117)
    rec=Polygon(pt1,pt2,pt3,pt4)
    rec.setFill(color_rgb(133,0,208 ))
    rec.draw(win)

    pt1 = Point(83,98)
    pt2 = Point(113,98)
    pt3 = Point(108,92)
    pt4 = Point(78,92)
    rec=Polygon(pt1,pt2,pt3,pt4)
    rec.setFill(color_rgb(250,250,250 ))
    rec.draw(win)

    pt1 = Point(87,70)
    pt2 = Point(117,70)
    pt3 = Point(77,53)
    pt4 = Point(47,53)
    rec=Polygon(pt1,pt2,pt3,pt4)
    rec.setFill(color_rgb(133,0,208 ))
    rec.draw(win)

    pt1 = Point(112,70)
    pt2 = Point(142,70)
    pt3 = Point(102,53)
    pt4 = Point(72,53)
    rec=Polygon(pt1,pt2,pt3,pt4)
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
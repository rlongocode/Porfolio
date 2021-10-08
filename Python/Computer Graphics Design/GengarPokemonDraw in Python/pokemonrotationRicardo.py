from time import sleep
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
# This is y-z rotation in y-z plane
# centers of rotation with respect to middle section of snowman  
    cx = (63+ 127)/2
    cy = (52 +155)/2
    cz = 0

#projection factor
    ff1 = .5*math.cos(75/180*math.pi)

    for  mm  in range(0,360,5):
       pt1 = Point(75,115)  
       pt2 = Point(115,73)  
       pt3 = Point(75,73)
       pt4 = Point(115,115)
       x1 = pt1.x
       x2 = pt2.x
       x3 = pt3.x
       x4 = pt4.x     
      
     
          
       yn1,zn1=rot(pt1.y,0,mm,cy,cz)
       yn2,zn2=rot(pt2.y,0,mm,cy,cz)
       yn3,zn3=rot(pt3.y,0,mm,cy,cz)
       yn4,zn4=rot(pt4.y,0,mm,cy,cz)
       xo1 = x1 + ff1 *zn1
       yo1 = yn1+ ff1*zn1

       xo2 = x2 + ff1 *zn2
       yo2 = yn2+ ff1*zn2
     
       xo3 = x3 + ff1 *zn3
       yo3 = yn3+ ff1*zn3

       xo4 = x4 + ff1 *zn4
       yo4 = yn4+ ff1*zn4

       pt1 = Point(xo1,yo1)
       pt2 = Point(xo2,yo2)
       pt3 = Point(xo3,yo3)
       pt4 = Point(xo4,yo4)      
       rec1=Polygon(pt1,pt4,pt2,pt3)
       rec1.setFill(color_rgb(133,0,208 ))
       rec1.draw(win)

       pt1 = Point(68,115)
       pt2 = Point(73,93)
       pt3 = Point(68,93)
       pt4= Point(73,115)
       x1 =pt1.x
       x2 = pt2.x
       x3 = pt3.x
       x4 = pt4.x
       yn1,zn1=rot(pt1.y,0,mm,cy,cz)
       yn2,zn2=rot(pt2.y,0,mm,cy,cz)
       yn3,zn3=rot(pt3.y,0,mm,cy,cz)
       yn4,zn4=rot(pt4.y,0,mm,cy,cz)
       xo1 = x1 + ff1 *zn1
       yo1 = yn1+ ff1*zn1

       xo2 = x2 + ff1 *zn2
       yo2 = yn2+ ff1*zn2
     
       xo3 = x3 + ff1 *zn3
       yo3 = yn3+ ff1*zn3
     
       xo4 = x4 + ff1 *zn4
       yo4 = yn4+ ff1*zn4
           

       pt1 = Point(xo1,yo1)
       pt2 = Point(xo2,yo2)
       pt3 = Point(xo3,yo3)
       pt4 = Point(xo4,yo4)
       rec2=Polygon(pt1,pt4,pt2,pt3)
       rec2.setFill(color_rgb(133,0,208 ))
       rec2.draw(win)

       pt1 = Point(117,115)
       pt2 = Point(122,93)
       pt3 = Point(117,93)
       pt4 = Point(122,115)
       x1 =pt1.x
       x2 = pt2.x
       x3 = pt3.x
       x4 = pt4.x
       yn1,zn1=rot(pt1.y,0,mm,cy,cz)
       yn2,zn2=rot(pt2.y,0,mm,cy,cz)
       yn3,zn3=rot(pt3.y,0,mm,cy,cz)
       yn4,zn4=rot(pt4.y,0,mm,cy,cz)
       xo1 = x1 + ff1 *zn1
       yo1 = yn1+ ff1*zn1

       xo2 = x2 + ff1 *zn2
       yo2 = yn2+ ff1*zn2
     
       xo3= x3 + ff1 *zn3
       yo3 = yn3+ ff1*zn3

       xo4 = x4 + ff1 *zn4
       yo4 = yn4+ ff1*zn4

       pt1 = Point(xo1,yo1)
       pt2 = Point(xo2,yo2)
       pt3 = Point(xo3,yo3)
       pt4 = Point(xo4,yo4)
       rec3=Polygon(pt1,pt4,pt2,pt3)
       rec3.setFill(color_rgb(133,0,208 ))
       rec3.draw(win)


       pt1 = Point(85,135)
       pt2 = Point(95,117)
       pt3 = Point(85,117)
       pt4 = Point(95,135)
       x1 = pt1.x
       x2 = pt2.x
       x3 = pt3.x
       x4 = pt4.x
       yn1,zn1=rot(pt1.y,0,mm,cy,cz)
       yn2,zn2=rot(pt2.y,0,mm,cy,cz)

       yn3,zn3=rot(pt3.y,0,mm,cy,cz)
       yn4,zn4=rot(pt4.y,0,mm,cy,cz)

       xo1 = x1 + ff1 *zn1
       yo1 = yn1+ ff1*zn1

       xo2 = x2 + ff1 *zn2
       yo2 = yn2+ ff1*zn2

       xo3 = x3 + ff1 *zn3
       yo3 = yn3+ ff1*zn3

       xo4 = x4 + ff1 *zn4
       yo4 = yn4+ ff1*zn4
     
      

       pt1 = Point(xo1,yo1)
       pt2 = Point(xo2,yo2)
       pt3 = Point(xo3,yo3)
       pt4 = Point(xo4,yo4)
       rec4=Polygon(pt1,pt4,pt2,pt3)
       rec4.setFill(color_rgb(133,0,208 ))
       rec4.draw(win)

       pt1 = Point(97,135)
       pt2 = Point(107,117)
       pt3 = Point(97,117)
       pt4 = Point(107,135)
       x1 =pt1.x
       x2 = pt2.x
       x3 = pt3.x
       x4 = pt4.x
       yn1,zn1=rot(pt1.y,0,mm,cy,cz)
       yn2,zn2=rot(pt2.y,0,mm,cy,cz)
       yn3,zn3=rot(pt3.y,0,mm,cy,cz)
       yn4,zn4=rot(pt4.y,0,mm,cy,cz)
       xo1 = x1 + ff1 *zn1
       yo1 = yn1+ ff1*zn1

       xo2 = x2 + ff1 *zn2
       yo2 = yn2+ ff1*zn2
     
       xo3 = x3 + ff1 *zn3
       yo3 = yn3+ ff1*zn3

       xo4 = x4 + ff1 *zn4
       yo4 = yn4+ ff1*zn4

       pt1 = Point(xo1,yo1)
       pt2 = Point(xo2,yo2)
       pt3 = Point(xo3,yo3)
       pt4 = Point(xo4,yo4)
       rec5=Polygon(pt1,pt4,pt2, pt3)
       rec5.setFill(color_rgb(133,0,208 ))
       rec5.draw(win)

       pt1 = Point(83,98)
       pt2 = Point(108,92)
       pt3 = Point(83,92)
       pt4 = Point(108,98)
       x1 = pt1.x
       x2 = pt2.x
       x3 = pt3.x
       x4 = pt4.x
       yn1,zn1=rot(pt1.y,0,mm,cy,cz)
       yn2,zn2=rot(pt2.y,0,mm,cy,cz)
       yn3,zn3=rot(pt3.y,0,mm,cy,cz)
       yn4,zn4=rot(pt4.y,0,mm,cy,cz)

       xo1 = x1 + ff1 *zn1
       yo1 = yn1+ ff1*zn1

       xo2 = x2 + ff1 *zn2
       yo2 = yn2+ ff1*zn2

       xo3 = x3 + ff1 *zn3
       yo3 = yn3+ ff1*zn3

       xo4 = x4 + ff1 *zn4
       yo4 = yn4+ ff1*zn4
       pt1 = Point(xo1,yo1)
       pt2 = Point(xo2,yo2)
       pt3 = Point(xo3,yo3)
       pt4 = Point(xo4,yo4)
       rec6=Polygon(pt1,pt4,pt2,pt3)
       rec6.setFill(color_rgb(255,255,255 ))
       rec6.draw(win)

       pt1 = Point(87,70)  
       pt2 = Point(77,53)  
       pt3 = Point(87,53)
       pt4 = Point(77,70)
       x1 = pt1.x
       x2 = pt2.x
       x3 = pt3.x
       x4 = pt4.x     
      
     
          
       yn1,zn1=rot(pt1.y,0,mm,cy,cz)
       yn2,zn2=rot(pt2.y,0,mm,cy,cz)
       yn3,zn3=rot(pt3.y,0,mm,cy,cz)
       yn4,zn4=rot(pt4.y,0,mm,cy,cz)
       xo1 = x1 + ff1 *zn1
       yo1 = yn1+ ff1*zn1

       xo2 = x2 + ff1 *zn2
       yo2 = yn2+ ff1*zn2
     
       xo3 = x3 + ff1 *zn3
       yo3 = yn3+ ff1*zn3

       xo4 = x4 + ff1 *zn4
       yo4 = yn4+ ff1*zn4

       pt1 = Point(xo1,yo1)
       pt2 = Point(xo2,yo2)
       pt3 = Point(xo3,yo3)
       pt4 = Point(xo4,yo4)      
       rec7=Polygon(pt1,pt4,pt2,pt3)
       rec7.setFill(color_rgb(133,0,208 ))
       rec7.draw(win)

       pt1 = Point(112,70)  
       pt2 = Point(102,53)  
       pt3 = Point(112,53)
       pt4 = Point(102,70)
       x1 = pt1.x
       x2 = pt2.x
       x3 = pt3.x
       x4 = pt4.x     
      
     
          
       yn1,zn1=rot(pt1.y,0,mm,cy,cz)
       yn2,zn2=rot(pt2.y,0,mm,cy,cz)
       yn3,zn3=rot(pt3.y,0,mm,cy,cz)
       yn4,zn4=rot(pt4.y,0,mm,cy,cz)
       xo1 = x1 + ff1 *zn1
       yo1 = yn1+ ff1*zn1

       xo2 = x2 + ff1 *zn2
       yo2 = yn2+ ff1*zn2
     
       xo3 = x3 + ff1 *zn3
       yo3 = yn3+ ff1*zn3

       xo4 = x4 + ff1 *zn4
       yo4 = yn4+ ff1*zn4

       pt1 = Point(xo1,yo1)
       pt2 = Point(xo2,yo2)
       pt3 = Point(xo3,yo3)
       pt4 = Point(xo4,yo4)      
       rec8=Polygon(pt1,pt4,pt2,pt3)
       rec8.setFill(color_rgb(133,0,208 ))
       rec8.draw(win)
  
      
       pt1 = Point(87,77)  
       pt2 = Point(77,87)  
       pt3 = Point(87,87)
       pt4 = Point(77,77)
       x1 = pt1.x
       x2 = pt2.x
       x3 = pt3.x
       x4 = pt4.x     

       yn1,zn1=rot(pt1.y,0,mm,cy,cz)
       yn2,zn2=rot(pt2.y,0,mm,cy,cz)
       yn3,zn3=rot(pt3.y,0,mm,cy,cz)
       yn4,zn4=rot(pt4.y,0,mm,cy,cz)
       xo1 = x1 + ff1 *zn1
       yo1 = yn1+ ff1*zn1

       xo2 = x2 + ff1 *zn2
       yo2 = yn2+ ff1*zn2
     
       xo3 = x3 + ff1 *zn3
       yo3 = yn3+ ff1*zn3

       xo4 = x4 + ff1 *zn4
       yo4 = yn4+ ff1*zn4

       pt1 = Point(xo1,yo1)
       pt2 = Point(xo2,yo2)
       pt3 = Point(xo3,yo3)
       pt4 = Point(xo4,yo4)      
       rec10=Polygon(pt1,pt4,pt2,pt3)
       rec10.setFill(color_rgb(255,0,0 ))
       rec10.draw(win)



       pt1 = Point(112,77)  
       pt2 = Point(102,87)  
       pt3 = Point(112,87)
       pt4 = Point(102,77)
       x1 = pt1.x
       x2 = pt2.x
       x3 = pt3.x
       x4 = pt4.x     
 
       yn1,zn1=rot(pt1.y,0,mm,cy,cz)
       yn2,zn2=rot(pt2.y,0,mm,cy,cz)
       yn3,zn3=rot(pt3.y,0,mm,cy,cz)
       yn4,zn4=rot(pt4.y,0,mm,cy,cz)
       xo1 = x1 + ff1 *zn1
       yo1 = yn1+ ff1*zn1

       xo2 = x2 + ff1 *zn2
       yo2 = yn2+ ff1*zn2
     
       xo3 = x3 + ff1 *zn3
       yo3 = yn3+ ff1*zn3

       xo4 = x4 + ff1 *zn4
       yo4 = yn4+ ff1*zn4

       pt1 = Point(xo1,yo1)
       pt2 = Point(xo2,yo2)
       pt3 = Point(xo3,yo3)
       pt4 = Point(xo4,yo4)      
       rec11=Polygon(pt1,pt4,pt2,pt3)
       rec11.setFill(color_rgb(255,0,0 ))
       rec11.draw(win)
          
      


       sleep(0.5)
       rec1.undraw()
       rec2.undraw()
       rec3.undraw()
       rec4.undraw()
       rec5.undraw()
       rec6.undraw()
       rec7.undraw()
       rec8.undraw()
       rec10.undraw()
       rec11.undraw()
       
# components of snowman
    win.getMouse()
    win.close()
       


# need to draw circle2 as a set of points not using built in function and rotate them, or make eyes square
#    pt= Point(90,80)
#    cir = Circle(pt,3)
#    cir.setFill(color_rgb(255,0,0 ))
#    cir.draw(win)

#    pt= Point(100,80)
#    cir = Circle(pt,3)
#    cir.setFill(color_rgb(255,0,0 ))
#    cir.draw(win)

def rot(x , y , jj ,cx ,cy):
       print(jj)
       X0 = x
       Y0 = y
       th0 = jj / 180 * 3.14159
       x = (X0 - cx) * math.cos(th0) - (Y0 - cy) * math.sin(th0)
       y = (X0 - cx) * math.sin(th0) + (Y0 - cy) * math.cos(th0)

       xn = x + cx
       yn = y + cy
       return xn,yn
    

main()
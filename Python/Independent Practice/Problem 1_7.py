#Ricardo Longo

def problem1_7():

    basea = float(input("Enter the length of one of the bases: "))
    baseb = float(input("Enter the Length of the other base: "))
    
    h = float(input("Enter the height: "))
    
    area = basea + baseb
    area = area * h
    area = area * 0.5
    
    print("The area of a trapezoid with bases",basea,"and",baseb,"and height",h,"is",area)

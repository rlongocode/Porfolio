
def problem2_7():
    """ computes area of triangle using Heron's formula. """
    a = float(input("Enter the length of side one: "))
    b = float(input("Enter the Length of side two: "))
    c = float(input("Enter the Length of side three: "))
    
    s = (a + b + c)/2
    
    areatriangle = s*((s-a)*(s-b)*(s-c))
    
    print("Area of a triangle with sides",a,b,c,"is",areatriangle**0.5)
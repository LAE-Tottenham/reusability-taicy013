import math
def valid(entry):
    check = False
    while not check:
        count = 0
        for x in entry:
            if x.isalpha() or x in '}/$!&*()_-+=[]{#~@''""\\|<>,:;£%? ':
                count = 1
                break
        if count != 1:
            check = True
        else:
            entry = input("Invalid. Enter again: ")
    return entry
def pick_tri(tri1,tri2):
    t = input("Triangle 1 or 2? (Enter 1 or 2): ")
    t = valid(t)
    if int(t) == 1:
        return tri1
    else:
        return tri2
def user_triangle():
    op = input("Enter triangle's opposite side length: ")
    op = valid(op)
    adj = input("Enter triangle's adjacent side length: ")
    adj = valid(adj)
    return [float(op),float(adj)]
def hyp(arr):
    return math.sqrt(arr[0]**2 + arr[1]**2)



def sin_angle(o,h):
    return math.degrees(math.asin(o/h))
def cos_angle(a,h):
    return math.degrees(math.acos(a/h))
def tan_angle(o,a):
    return math.degrees(math.acos(o/a))
def missing_angle(tri):
    func = input("Enter trig ratio you would like to use: (s for sine, c for cos, t for tan) ")
    func = func.lower()
    if func == 's':
        return "Angle in degrees: ", sin_angle(tri[0],hyp(tri))
    elif func == 'c':
        return "Angle in degrees: ", cos_angle(tri[1],hyp(tri))
    else:
        return "Angle in degrees: ", tan_angle(tri[0],tri[1])

def sin_rule(tri):
    a = tri[0]
    sina = tri[0]/hyp(tri)
    sinb = 1
    return "Hypotenuse, using sine rule: ", (a*sinb)/(sina)
def cosine_rule(tri):
    b = tri[0]
    c = tri[1]
    cosa = 0
    return "Hypotenuse, using cosine rule: ", math.sqrt((b**2)+(c**2)+(-2*b*c*cosa))

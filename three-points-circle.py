import re
import math
def checkio(data):

    #replace this for solution
    p = (int(pstr) for pstr in re.sub(r'\(|\)', '', data).split(","))
    (x1, y1), (x2, y2), (x3, y3) = (list(zip(p, p)))

    p = ((y1-y3)*(y1**2 -y2**2 +x1**2 -x2**2) -(y1-y2)*(y1**2 -y3**2 +x1**2 -x3**2)) / (2*(y1-y3)*(x1-x2)-2*(y1-y2)*(x1-x3))
    q = ((x1-x3)*(x1**2 -x2**2 +y1**2 -y2**2) -(x1-x2)*(x1**2 -x3**2 +y1**2 -y3**2)) / (2*(x1-x3)*(y1-y2)-2*(x1-x2)*(y1-y3))
    r = math.sqrt((x1-p)**2 + (y1-q)**2)

    formula = "(x{})^2+(y{})^2={}^2".format(num_fmt(p), num_fmt(q), num_fmt(r, with_sign=False))
    print(formula)
    return formula

def num_fmt(n, with_sign=True):
    if with_sign:
        sign = "+" if n < 0 else "-"
        n = abs(n)
    else:
        sign = ""

    return sign + re.sub(r'\.0$', '', str(round(n, 2)))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    assert checkio("(4,4),(4,8),(3,10)") == "(x+2.5)^2+(y-6)^2=6.8^2"

__author__ = 'Nickolas'


def corner(m, n):
    x= n*("+"+"-"*m)+"+\n"
    return(x)


def vertical(m, n):
    x= n*("|"+" "*m)+"|\n"
    return(x)


def boxes(m, n, x, y):
    g=(corner(m, n)+(vertical(m, n)*y))*x + (corner(m, n))
    return (g)

m=0
print(boxes(2, 3, 4, 5))
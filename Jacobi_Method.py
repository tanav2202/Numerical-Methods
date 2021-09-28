
# defining equations to be solved
# in diagonally dominant form
# Reads two numbers from input and typecasts them to int using 
# map function

x1,y1,z1,d1 = map(int, input("x1 y1 z1 d1 :").split())
x2,y2,z2,d2 = map(int, input("x2 y2 z2 d2 :").split())
x3,y3,z3,d3 = map(int, input("x3 y3 z3 d3 :").split())

# three lambda function that will produces required values
f1 = lambda x,y,z,d1,x1,y1,z1: (d1-(y1*y+z1*z))/x1
f2 = lambda x,y,z,d2,x2,y2,z2: (d2-(x2*x+z2*z))/y2
f3 = lambda x,y,z,d3,x3,y3,z3: (d3-(x3*x+y3*y))/z3


# initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# reading tolerable error
e = float(input('enter tolerable error: '))


print('\ncount\tx\ty\tz\n')

condition = True

# implementation of jacobi iteration
while condition:
    xp = f1(x0,y0,z0,d1,x1,y1,z1)
    yp = f2(x0,y0,z0,d2,x2,y2,z2)
    zp = f3(x0,y0,z0,d3,x3,y3,z3)
    print('%d\t%f\t%f\t%f\n' %(count, xp,yp,zp))
    e1 = abs(x0-xp);
    e2 = abs(y0-yp);
    e3 = abs(z0-zp);
    
    count += 1
    x0 = xp
    y0 = yp
    z0 = zp
# condition checks if the accuracy of results are met
    condition = e1>e and e2>e and e3>e

print('\nsolution: x=%f, y=%f and z = %f'% (xp,yp,zp))



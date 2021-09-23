from math import * 
from sympy import symbols,diff
from sympy.abc import x,y


# def standardNR():
#     print ("standard nr")
#     f = input("enter f(x) in pyth n syntax,ie. x^2 as x**2 , write math functions as func() , like exp(), tan().\n \n")

def standardNR():
    print("standard nr")
    f = input("enter f(x) in pyth n syntax,ie. x^2 as x**2 , write math  functions as func() , like exp(), tan().\n \n")
    fx = diff(f, x)
    lf = eval("lambda x:"+str(f))
    lfx = eval("lambda x:"+str(fx))
    x_0 = float(input("x0 :"))
    h=lambda x: x - lf(x)/lfx(x)

    print ("n \t x1  \t\t x2  ")
    counter = 1
    while (abs (( x_0-h(x_0))) >= 0.00001) :

        hv = h(x_0)
        print(counter,"\t",'%.5f'%x_0,"\t",'%.5f'%hv,"\t")
        counter +=1
        x_0=h(x_0)


    print("The value of root is : ",'%.5f'%x_0,)


def non_HomoNR():
    f = input("enter f(x,y) in pyth n syntax,ie. x^2 as x**2 , write math functions as func() , like exp(), tan(). \n")
    g = input("enter g(x,y) expression in python syntax,ie. x^2 as x**2 , write math functions as func() , like exp(), tan(). \n")
    x_0,y_0 = map(float, input("x0 y0 :").split())

    fx = diff(f,x)
    fy = diff(f,y)
    gx = diff(g,x)
    gy = diff(g,y)
    lf= eval("lambda x,y:"+str(f))
    lg= eval("lambda x,y:"+str(g))
    lfx= eval("lambda x,y:"+str(fx))
    lgx= eval("lambda x,y:"+str(gx))
    lfy= eval("lambda x,y:"+str(fy))
    lgy= eval("lambda x,y:"+str(gy))
    counter = 0
    # print("n\t    a\t\t  f(a)\t\t  b\t"+"  "+"\tf(b)\t\t  c=(a+b)/2\t  f(c)\t\tupdate")

    # print(fx,gx,fy,gy)
    h = lambda x,y: ((lg(x,y)*lfy(x,y)-lf(x,y)*lgy(x,y))/\
            (lfx(x,y)*lgy(x,y)-lgx(x,y)*lfy(x,y)))
    k = lambda x,y: ((lf(x,y)*lgx(x,y)-lg(x,y)*lfx(x,y))/\
            (lfx(x,y)*lgy(x,y)-lgx(x,y)*lfy(x,y)))

    # print(h(x_0,y_0),k(x_0,y_0),f , g)
    print ("n \t x \t\t y \t\t h \t\t k ")
    while (abs((h(x_0,y_0)+k(x_0,y_0))) >= 0.00002):

        hv = h(x_0,y_0)
        kv = k(x_0,y_0)
        print(counter,"\t",'%.5f'%x_0,"\t",'%.5f'%y_0,"\t" ,'%.5f'%hv,"\t" , '%.5f'%kv)
        counter +=1
        x_0=x_0+h(x_0,y_0)
        y_0=y_0+k(x_0,y_0)



    print("The value of root is : ",'%.5f'%x_0,'%.5f'%y_0)





def main():
    print("Starting.........")
    # a , b  = map(int, input("enter a b :").split())
    # case=input("enter 1 for single variable(does not work) and 2 for multi \t")
    # if case == 1:
    #     standardNR()
    # else :
    #     non_HomoNR()

    standardNR()

    # bisection(a, b)

if __name__ == "__main__":
    main()

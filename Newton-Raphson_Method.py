from math import * 
from sympy import symbols,diff
from sympy.abc import x,y
import inspect
# inspect.getsource(myfunc)

# input lelo lambda
# fir x0 y0 input lelo
# initial h or k ki value calc karo
# x = x+h ~~~~ y

def standardNR():
    print ("standard nr")




def non_HomoNR():
    f = input("enter f(x,y) in pyth n syntax,ie. x^2 as x**2 , write math functions as func() , like exp(), tan(). \n")
    g = input("enter g(x,y) expression in python syntax,ie. x^2 as x**2 , write math functions as func() , like exp(), tan(). \n")
    x_0,y_0 = map(float, input("x0 y0 :").split())
    # x,y=symbols('x y',real=True) 
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
    while (abs((h(x_0,y_0)+k(x_0,y_0))) >= 0.00002):
        counter +=1
        # print(counter,"\t",'%.5f'%a,"\t",'%.5f'%func(a),"\t",'%.5f'%b,"\t",'%.5f'%func(b),"\t",'%.5f'%c,"\t",'%.5f'%func(c),"\t",update)
        hv = h(x_0,y_0)
        kv = k(x_0,y_0)
        print("h : ",hv,"k: ",kv)
        x_0=x_0+h(x_0,y_0)
        y_0=y_0+k(x_0,y_0)



    print("The value of root is : ",x_0,y_0)



def main():
    print("Starting.........")
    # a , b  = map(int, input("enter a b :").split())
    case=input("enter 1 for single variable(does not work) and 2 for multi \t")
    if case == 1:
        standardNR()
    else :
        non_HomoNR()


    # bisection(a, b)

if __name__ == "__main__":
    main()
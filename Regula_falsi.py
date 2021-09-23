from math import * 
from sympy import symbols,diff
from sympy.abc import x,y


def standardNR():
    print("standard nr")
    f = input("enter f(x) in pyth n syntax,ie. x^2 as x**2 , write math  functions as func() , like exp(), tan().\n \n")
    x_a,x_b = map(float, input("range a b :").split())
    lf = eval("lambda x:"+str(f))



    print("The value of root is : ",'%.5f'%x_0,)


def main():
    print("Starting.........")

    standardNR()


if __name__ == "__main__":
    main()

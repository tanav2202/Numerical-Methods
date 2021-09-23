from math import * 


def bisection(a,b):
    func = eval("lambda x:"+input("enter expression in python syntax,ie. x^2 as x**2 , write math functions as func() , like exp(), tan(). \n"))
    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    counter = 0
    print("n\t    a\t\t  f(a)\t\t  b\t"+"  "+"\tf(b)\t\t  c=(a+b)/2\t  f(c)\t\tupdate")
    update=""
    while ((b-a) >= 0.00001):
        print(counter,"\t",'%.5f'%a,"\t",'%.5f'%func(a),"\t",'%.5f'%b,"\t",'%.5f'%func(b),"\t",'%.5f'%c,"\t",'%.5f'%func(c),"\t",update)
        # Find middle point
        c = (a+b)/2
        # Check if middle point is root
        if (func(c) == 0.0):
            break

        # Decide the side to repeat the steps
        if (func(c)*func(a) < 0):
            b = c
            update = "b = c"
        else:
            a = c
            update = "a = c"
        counter +=1

    print("The value of root is : ","%.4f"%c)



def main():
    print("Starting")
    a , b  = map(float, input("enter a b :").split())
    bisection(a, b)



if __name__ == "__main__":
    main()




def Regula():
    print("\n")
    f = input("enter f(x) in pyth n syntax,ie. x^2 as x**2 , \
            write math  functions as func() , like exp(), tan().\n")
    x_0, x_1 = map(float, input("range a to b :").split())
    e = float(input('enter tolerable error: '))
    lf = eval("lambda x:"+str(f))
    def h(x0, x1): return x1 - (x1-x0) * lf(x1) / \
        (lf(x1) - lf(x0))
    print("\n")
    counter = 1
    while (abs((x_1-h(x_0, x_1))) >= e):

        tmp = x_1
        x_1 = h(x_0, x_1)
        if lf(x_1) > 0:
            x_0 = tmp

        counter += 1
        print("x"+str(counter)+" ==>  ", '%.5f' %
              x_1, "\t f(x"+str(counter)+") ==>  ", '%.5f' % lf(x_1))

    print("The value of root is x", counter, " is :", '%.5f' % x_1)


def main():
    print("Starting.........")
    Regula()


if __name__ == "__main__":
    main()

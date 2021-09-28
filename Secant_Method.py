

def SecantM():
    print("\n")
    f = input("enter f(x) in pyth n syntax,ie. x^2 as x**2 , \
            write math  functions as func() , like exp(), tan().\n")
    x_0, x_1 = map(float, input("range a to b :").split())
    e = float(input('enter tolerable error: '))
    lf = eval("lambda x:"+str(f))
    def h(x0, x1): return x1 - (x1-x0) * lf(x1) / \
        (lf(x1) - lf(x0))

    counter = 1
    while (abs((x_1-h(x_0, x_1))) >= e):
        print("x", counter, "\t", '%.5f' % x_1)
        tmp = x_1
        x_1 = h(x_0, x_1)
        x_0 = tmp
        counter += 1

    print("The value of root is x", counter, " is :", '%.5f' % x_1)


def main():
    print("Starting.........")
    SecantM()


if __name__ == "__main__":
    main()

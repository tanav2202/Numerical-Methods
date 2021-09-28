
def seidel(a, x, b):
    # Finding length of a(3)
    n = len(a)
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if(j != i):
                d -= a[j][i] * x[i]
        # updating the value of our solution
        x[j] = d / a[j][j]
    # returning our updated solution
    return x


# int(input())input as number of variable to be solved
n = 3
a = []
b = []
# initial solution depending on n(here n=3)
x1, y1, z1, d1 = map(int, input("x1 y1 z1 d1 :").split())
x2, y2, z2, d2 = map(int, input("x2 y2 z2 d2 :").split())
x3, y3, z3, d3 = map(int, input("x3 y3 z3 d3 :").split())
x = [0, 0, 0]
a = [[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]]
b = [d1, d2, d3]
print(x)
counter = 0
# loop run for m times depending on m the error value
for i in range(0, 15):
    x = seidel(a, x, b)
    # print each time the updated solution
    print()
    counter += 1
    print(counter, end="")
    print('\t', end="")
    for i in range(3):
        print('%.5f' % x[i], '   ', end="")
    print()

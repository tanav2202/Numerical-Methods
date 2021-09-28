import numpy as np
x1, y1, z1, d1 = map(int, input("x1 y1 z1 d1 :").split())
x2, y2, z2, d2 = map(int, input("x2 y2 z2 d2 :").split())
x3, y3, z3, d3 = map(int, input("x3 y3 z3 d3 :").split())

# initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1


def crout(A):
    L = np.zeros((3, 3))
    U = np.zeros((3, 3))
    for k in range(0, 3):
        np.fill_diagonal(U, 1)

        for j in range(k, 3):
            sum0 = sum([L[j, s] * U[s, k] for s in range(0, k)])
            L[j, k] = A[j, k] - sum0

        for j in range(k+1, 3):
            sum1 = sum([L[k, s] * U[s, j] for s in range(0, k)])
            U[k, j] = (A[k, j] - sum1) / L[k, k]

    print(L)
    print()
    print(U)
    # Y = np/zeros((1, 3))


A = np.array(
    [
        [x1, y1, z1],
        [x2, y2, z2],
        [x3, y3, z3]
    ]
)
crout(A)

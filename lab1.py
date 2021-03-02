import numpy as np
def swap(v, x, y):
    t = v[x].copy()
    v[x] = v[y]
    v[y] = t
def G_method_build_mat(Mat, n, B):
    for i in range(n):
        for j in range(n - 1 - i):
            jj = n - 1 - j
            k = Mat[jj, i] / Mat[i, i]
            Mat[jj] -= Mat[i] * k
            B[jj] -= B[i] * k

def G_method_full_max_build_mat(Mat, n, B):
    for i in range(n):
        for ii in range(n - i - 1):
            for jj in range(n - i - 2):
                if(Mat[jj + i, i] < Mat[jj + i + 1, i]):
                    swap(Mat, jj + i, jj + i + 1)
                    B [jj + i],B[jj + i + 1] = B[jj + i + 1] ,B[jj + i]
        for j in range(n - 1 - i):
            jj = n - 1 - j
            k = Mat[jj, i] / Mat[i, i]
            Mat[jj] -= Mat[i] * k
            B[jj] -= B[i] * k

def G_method_max_build_mat(Mat, n, B):
    for i in range(n):
        for ii in range(n - i - 2):
            for jj in range(n - i - 3):
                if(Mat[jj + i, i] < Mat[jj + i + 1, i]):
                    swap(Mat, jj + i + 1, jj + i + 2)
                    B [jj + i + 1],B[jj + i + 2] = B[jj + i + 2] ,B[jj + i + 1]
        for j in range(n - 1 - i):
            jj = n - 1 - j
            k = Mat[jj, i] / Mat[i, i]
            Mat[jj] -= Mat[i] * k
            B[jj] -= B[i] * k

def G_method_solve(mat, B, n, ans):
    for i in range(n):
        ii = n - 1 - i
        temp = B[ii]
        for j in range(n):
            temp -= mat[ii, j] * ans[j]
        ans[ii] = temp / mat[ii, ii]

b = [4.2, 4.2, 4.2, 4.2, 4.2]
C = np.matrix([[0.2, 0, 0.2, 0, 0],[0, 0.2, 0, 0.2, 0],[0.2, 0, 0.2, 0, 0.2],[0, 0.2, 0, 0.2, 0],[0, 0, 0.2, 0, 0.2]])
D = np.matrix([[2.33, 0.81, 0.67, 0.92, -0.53],[-0.53, 2.33, 0.81, 0.67, 0.92],[0.92, -0.53, 2.33, 0.81, 0.67],[0.67, 0.92, -0.53, 2.33, 0.81],[0.81, 0.67, 0.92, -0.53, 2.33]])
A =  9 * C + D
X = [0, 0, 0, 0, 0]

'''
A = np.matrix([
    [1.0, 1.0],
    [1.0, -1.0]
])
b = [2, 4]
X = [0, 0]
'''
A1 = A.copy()
A2 = A.copy()
A3 = A.copy()
b1 = b.copy()
b2 = b.copy()
b3 = b.copy()
X1 = X.copy()
X2 = X.copy()
X3 = X.copy()
G_method_build_mat(A1, 5, b1)
G_method_solve(A1, b1, 5, X1)
print(X1)
G_method_max_build_mat(A2, 5, b2)
G_method_solve(A2, b2, 5, X2)
print(X2)
G_method_full_max_build_mat(A3, 5, b3)
G_method_solve(A3, b3, 5, X3)
print(X3)


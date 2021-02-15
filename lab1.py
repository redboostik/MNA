import numpy as np
def swap(v, x, y):
    t = v[x].copy()
    v[x] = v[y]
    v[y] = t
def G_method_build_mat(Mat):
    for i in range(5):
        
        for ii in range(5 - i):
            for jj in range(4 - i):
               
                if(abs(Mat[jj + i, i]) < abs(Mat[jj + i + 1, i])):
                    swap(Mat, jj + i , jj + i + 1)
        for j in range(4 -i ):
            jj = 4-j
            Mat[jj] -= Mat[jj - 1] * Mat[jj, i] / Mat[jj - 1, i]

def G_method_solve(mat, B, ans):
    for i in range(5):
        ii = 4 - i
        temp = B[ii]
        for j in range(5):
            temp -= mat[ii, j] * ans[j]
        ans[ii] = temp / mat[ii, ii]

b = [4.2, 4.2, 4.2, 4.2, 4.2]
C = np.matrix([[0.2, 0, 0.2, 0, 0],[0, 0.2, 0, 0.2, 0],[0.2, 0, 0.2, 0, 0.2],[0, 0.2, 0, 0.2, 0],[0, 0, 0.2, 0, 0.2]])
D = np.matrix([[2.33, 0.81, 0.67, 0.92, -0.53],[-0.53, 2.33, 0.81, 0.67, 0.92],[0.92, -0.53, 2.33, 0.81, 0.67],[0.67, 0.92, -0.53, 2.33, 0.81],[0.81, 0.67, 0.92, -0.53, 2.33]])

A =  9 * C + D
print(np.linalg.solve(A,b))
G_method_build_mat(A)
X_G_method = [0, 0, 0, 0, 0]
G_method_solve(A,b, X_G_method)
print(X_G_method)


import numpy as np

def Get_ans_iteration_method(ni, Ai, bi):
    xnew = list(range(1,  ni + 1))
    xpref = list(range(2,  ni + 2))
    step = 0
    while Check_to_continue(xnew, xpref,ni):
        xpref = xnew.copy()
        for i in range(0, ni):
            xnew[i] = 0
            xnew[i] += bi[i]
            for j in range(0, ni):
                if i != j:
                    xnew[i] -= Ai[i,j] * xpref[j]
            xnew[i] /= Ai[i,i]
        step += 1
    print ("iteration method")
    print ("x: ", xnew)
    print ("steps: ", step)

def Get_ans_Zeidel_method(ni, Ai, bi):
    xnew = list(range(1,  ni + 1))
    xpref = list(range(2,  ni + 2))
    step = 0
    while Check_to_continue(xnew, xpref,ni):
        xpref = xnew.copy()
        for i in range(0, ni):
            xnew[i] = 0
            xnew[i] += bi[i]
            for j in range(0, ni):
                if i != j:
                    xnew[i] -= Ai[i,j] * xnew[j]
            xnew[i] /= Ai[i,i]
        step += 1
    print ("iteration method")
    print ("x: ", xnew)
    print ("steps: ", step)


def Check_to_continue(m1, m2, nc):
    flag = False
    for i in range(0, nc):
        if abs(m1[i]- m2[i]) > 0.0001:
            flag = True
    return flag


# lab_varible
n = 5
b = [1.2, 2.2, 4.0, 0.0, -1.2]
C = np.matrix([[0.01, 0, -0.02, 0, 0],
               [0.01, 0.01, -0.02, 0, 0],
               [0, 0.01, 0.01, 0, -0.02],
               [0, 0, 0.01, 0.01, 0],
               [0, 0, 0, 0.01, 0.01]])
D = np.matrix([ [1.33, 0.21, 0.17, 0.12, -0.13],
                [-0.13, -1.33, 0.11, 0.17, 0.12],
                [0.12, -0.13, -1.33, 0.11, 0.17],
                [0.17, 0.12, -0.13, -1.33, 0.11],
                [0.11, 0.67, 0.12, -0.13, -1.33]])
A =  9 * C + D

'''
# test_varible_1
n = 2
A = np.matrix([[1, 1],
               [1, -1]])
b = [3, 1]
'''
'''
# test_varible_2
n = 2
A = np.matrix([[8, 4],
               [4, -8]])
b = [12, 3]
'''
Get_ans_iteration_method(n, A, b)
Get_ans_Zeidel_method(n, A, b)

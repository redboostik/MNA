import sympy as sp


def Shturm(expr, x, L, R):
    y = []
    y.append(expr)
    y.append(sp.diff(expr, x))
    while (True):
        k = sp.div(y[len(y)-2], y[len(y)-1])
        if k[1] == 0:
            break
        y.append(-k[1])

    L_change = -1
    R_change = -1
    L_sign = 0
    R_sign = 0
    for i in range(len(y)):
        varible = y[i].subs(x,L)
        if(varible < 0 and L_sign >= 0):
            L_sign = -1
            L_change += 1
        elif(varible > 0 and L_sign <= 0):
            L_sign = 1
            L_change += 1
        varible = y[i].subs(x,R)
        if(varible < 0 and R_sign >= 0):
            R_sign = -1
            R_change += 1
        elif(varible > 0 and R_sign <= 0):
            R_sign = 1
            R_change += 1
    return L_change, R_change

def half_method(expr, x, L, R, eps):
    steps = 0
    while(R - L > eps):
        steps += 1
        m = abs((R - L) / 2)
        la, no = Shturm(expr, x, L, R - m)
        if(la - no == 0) :
            L += m
        else:
            R -= m
    return L, steps

def get_func_res(expr, x, X):
    return expr.subs(x,X)

def chord_method(expr, x, L, R, eps):
    steps = 0
    if(get_func_res(expr, x, L) < 0):
        flag = True
    else:
        flag = False
    while (abs(get_func_res(expr,x,L)) > eps and abs(get_func_res(expr,x,R)) > eps ):
        steps += 1
        YL = get_func_res(expr, x, L)
        YR = get_func_res(expr, x, R)
        a = (YR - YL) / (R - L)
        b = YL - a * L 
        new_x = - b / a

        new_y = get_func_res(expr,x,new_x)
        if(new_y < 0):
            if(flag):
                L = new_x
            else:
                R = new_x
        else:
            if(flag):
                R = new_x
            else:
                L = new_x

    if(abs(YL)< eps):
        return L, steps
    else:
        return R, steps

def tangent_method(expr, diff,x,X, eps):
    steps = 0
    while(abs(get_func_res(expr,x,X))> eps):
        print(X, get_func_res(expr,x,X) / get_func_res(diff,x,X),get_func_res(expr, x, X))
        steps += 1
        X -= get_func_res(expr,x,X) / get_func_res(diff,x,X)
    return X, steps



x = sp.Symbol('x')
expr = 2.65804 * x**3 -28.0640 * x**2 + 21.9032 * x
eps = 0.000001
L_border = -10
R_border = 10
n, k = Shturm(expr, x, L_border, R_border)
range_corner = []
print("Корней: ",n)

for i in range(n):
    t = R_border - L_border
    print(L_border, R_border)
    new_L = L_border
    while( t > eps):
        la, no = Shturm(expr, x, new_L + t, R_border )
        if(la - no > 0):
            new_L += t
        t /= 2
    range_corner.append([new_L, R_border])
    R_border = new_L

print("Корни находятся в диапазонах: ", range_corner)

half_res, half_steps = half_method(expr, x, range_corner[n - 1][0],range_corner[n - 1][1], eps)
print("метод половинного деления: ")
print("ответ: ",half_res)
print("шагов: ",half_steps)

chord_res, chord_steps = chord_method(expr, x, range_corner[n - 1][0],range_corner[n - 1][1], eps)
print("метод хорд: ")
print("ответ: ",chord_res)
print("шагов: ",chord_steps)

tangent_res, tangent_steps = tangent_method(expr,sp.diff(expr, x), x,range_corner[n - 1][0], eps)
print("метод косательных: ")
print("ответ: ", tangent_res)
print("шагов: ", tangent_steps)
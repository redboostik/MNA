import numpy as np
import sympy as sp


def solve_x(x0, y0):
    return np.tan(x0 * y0 + m)


def solve_y(x0):
    return np.sqrt((1 - a * (x0 ** 2)) / 2)


def solve_yacobian(x0, y0):
    return np.array([
        [float(sp.diff(expr1, x).subs({x: x0, y: y0})), float(sp.diff(expr1, y).subs({x: x0, y: y0}))],
        [float(sp.diff(expr2, x).subs({x: x0, y: y0})), float(sp.diff(expr2, y).subs({x: x0, y: y0}))],
    ])


def Function(x0, y0):
    return np.array([
        [np.tan(x0 * y0 + 0.4) - x0],
        [0.7 * (x0 ** 2) + 2 * (y0 ** 2) - 1]
    ])


def check(a,b):

    if not(np.isfinite(a) and np.isfinite(b)):
            raise RuntimeError("Ошибка. Во время вычислений произашло переполнение.")


def solve_iterations_method(x0, y0):
    i = 0
    x, y = x0, y0
    while True:
        i += 1
        temp_x, temp_y = x, y
        x = solve_x(x, y)
        y = solve_y(x)
        check(x,y)
        if max(abs(x - temp_x), abs(y - temp_y)) < 0.00001 or i > 100000-1:
            return x, y, i


def solve_Newton_method(x0, y0):
    i = 0
    x, y = x0, y0
    while True:
        i += 1
        temp = np.linalg.solve(solve_yacobian(x, y), -Function(x, y))
        x += temp[0][0]
        y += temp[1][0]
        check(x,y)
        if max(abs(temp)) < 0.00001 or i > 100000:
            return x, y, i


m = 0.4
a = 0.7
e = 0.00001

(x, y) = sp.symbols('x y')

expr1 = sp.tan(x * y + m) - x
expr2 = a * (x ** 2) + 2 * (y ** 2) - 1

plots = sp.plot_implicit(sp.Eq(expr1, 0), (x, -5, 5), (y, -5, 5), line_color="green", show=False)
plots.extend(sp.plot_implicit(sp.Eq(expr2, 0), (x, -5, 5), (y, -5, 5), line_color="red", show=False))
plots.show()

approximately_x, approximately_y = 1, 0.35
x1, y1, i1 = solve_iterations_method(approximately_x, approximately_y)

x2, y2, i2 = solve_Newton_method(approximately_x, approximately_y)

print('Метод итераций: x:', x1, ', y:', y1, ', Кол-во итераций:', i1)

print('Метод Ньютона: x:', x2, ', y:', y2, ', Кол-во итераций:', i2)

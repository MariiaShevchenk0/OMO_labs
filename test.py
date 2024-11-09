import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 - 5.74 * x**3 + 8.18 * x - 3.48

x_vals = np.linspace(0.75, 0.25, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals)
plt.axhline(0, color='red', linestyle='--')
plt.title('Графік функції f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

def g(x):
    return (-x**4+5.74*x**3+3.48) / 8.18

def simple_iteration(g, x0, eps, max_iter=1000):
    iter_count = 0
    x_prev = x0
    x_next = g(x_prev)
    
    while abs(x_next - x_prev) > eps and iter_count < max_iter:
        x_prev = x_next
        x_next = g(x_prev)
        iter_count += 1
    
    return x_next, iter_count

x0 = 0.5
eps = 0.0001

root_iter, steps_iter = simple_iteration(g, x0, eps)
print(f"Корінь методом простої ітерації: {root_iter}, кількість ітерацій: {steps_iter}")

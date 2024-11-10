import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + np.sin(x) - 12*x - 0.25

# Функція для побудови графіка
# x_vals = np.linspace(-4, 4, 400)
# y_vals = f(x_vals)
# plt.plot(x_vals, y_vals)
# plt.axhline(0, color='red', linestyle='--')
# plt.title('Графік функції f(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.grid(True)
# plt.show()

# Метод дихотомії з апріорною оцінкою
def bisection_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        raise ValueError("Функція повинна змінювати знак на кінцях інтервалу.")
    
    # Апріорна оцінка кількості ітерацій
    apriori_estimate = int(np.ceil(np.log2((b - a) / tol)))
    print(f"Апріорна оцінка кількості ітерацій для методу дихотомії: {apriori_estimate}")
    
    iter_count = 0
    print("Метод дихотомії:")
    while (b - a) / 2 > tol:
        iter_count += 1
        c = (a + b) / 2
        print(f"Ітерація {iter_count}: c = {c}, f(c) = {f(c)}")
        if f(c) == 0:
            print("Знайдено точний корінь.")
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    print(f"Апостеріорна оцінка зупинилася на ітерації: {iter_count}")
    return (a + b) / 2, iter_count

a, b = -4, 4
eps = 0.0001

root_bisect, steps_bisect = bisection_method(f, a, b, eps)
print(f"Корінь методом дихотомії: {root_bisect}, кількість ітерацій: {steps_bisect}")

# Метод простої ітерації з апріорною оцінкою
def g(x):
    return (x**2 + np.sin(x) - 0.25) / 12

def simple_iteration(g, x0, eps, max_iter=1000):
    iter_count = 0
    x_prev = x0
    x_next = g(x_prev)
    
    # Апріорна оцінка для методу простої ітерації
    apriori_estimate = max_iter  # Для простої ітерації, оцінка залежить від властивостей функції g і точно оцінити не завжди можливо
    print(f"\nАпріорна оцінка кількості ітерацій для методу простої ітерації: {apriori_estimate}")
    
    print("Метод простої ітерації:")
    print(f"Ітерація {iter_count}: x = {x_prev}")
    while abs(x_next - x_prev) > eps and iter_count < max_iter:
        iter_count += 1
        x_prev = x_next
        x_next = g(x_prev)
        print(f"Ітерація {iter_count}: x = {x_next}")
    
    print(f"Апостеріорна оцінка зупинилася на ітерації: {iter_count}")
    return x_next, iter_count

x0 = 2

root_iter, steps_iter = simple_iteration(g, x0, eps)
print(f"Корінь методом простої ітерації: {root_iter}, кількість ітерацій: {steps_iter}")

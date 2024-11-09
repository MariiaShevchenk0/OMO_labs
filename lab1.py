import math

def f(x):
    return x**2 + math.sin(x) - 12*x - 0.25

def dichotomy_method(a, b, epsilon):
    steps = 0
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c, steps
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        steps += 1
    return (a + b) / 2, steps

def simple_iteration_method(x0, epsilon):
    def g(x):
        return (x**2 + math.sin(x) - 0.25) / 12
    
    x = x0
    steps = 0
    while True:
        x_new = g(x)
        if abs(x_new - x) < epsilon:
            return x_new, steps
        x = x_new
        steps += 1

def find_initial_interval():
    a, b = -20, 0
    while f(a) * f(b) > 0:
        a -= 1
        b += 1
    return a, b

def apriori_estimate_dichotomy(a, b, epsilon):
    return math.ceil(math.log2((b - a) / epsilon))

def aposteriori_estimate_dichotomy(a, b, n):
    return (b - a) / (2**n)

def apriori_estimate_simple_iteration(x0, epsilon):
    def g_prime(x):
        return (2*x + math.cos(x)) / 12
    
    x = x0
    q = abs(g_prime(x))
    for _ in range(100):
        x -= 0.1
        q = max(q, abs(g_prime(x)))
    
    if q >= 1:
        return "Метод може не збігатися, q >= 1"
    
    try:
        return math.ceil(math.log(epsilon * (1 - q) / abs(x - x0), q))
    except ValueError:
        return "Неможливо обчислити апріорну оцінку"

def aposteriori_estimate_simple_iteration(x_prev, x_curr, q):
    if q >= 1:
        return "Метод може не збігатися, q >= 1"
    return (q / (1 - q)) * abs(x_curr - x_prev)

def main():
    epsilon = 1e-4
    a, b = find_initial_interval()
    print(f"Початковий інтервал: [{a}, {b}]")
    
    root_dichotomy, steps_dichotomy = dichotomy_method(a, b, epsilon)
    print(f"\nМетод дихотомії:")
    print(f"Корінь: {root_dichotomy}")
    print(f"Кількість кроків: {steps_dichotomy}")
    print(f"f(x) = {f(root_dichotomy)}")
    
    apriori_dichotomy = apriori_estimate_dichotomy(a, b, epsilon)
    aposteriori_dichotomy = aposteriori_estimate_dichotomy(a, b, steps_dichotomy)
    print(f"Апріорна оцінка кількості кроків: {apriori_dichotomy}")
    print(f"Апостеріорна оцінка похибки: {aposteriori_dichotomy}")
    
    x0 = (a + b) / 2
    root_iteration, steps_iteration = simple_iteration_method(x0, epsilon)
    print(f"\nМетод простої ітерації:")
    print(f"Корінь: {root_iteration}")
    print(f"Кількість кроків: {steps_iteration}")
    print(f"f(x) = {f(root_iteration)}")
    
    apriori_iteration = apriori_estimate_simple_iteration(x0, epsilon)
    print(f"Апріорна оцінка кількості кроків: {apriori_iteration}")
    
    def g_prime(x):
        return (2*x + math.cos(x)) / 12
    q = abs(g_prime(root_iteration))
    
    x_prev = root_iteration - epsilon
    aposteriori_iteration = aposteriori_estimate_simple_iteration(x_prev, root_iteration, q)
    print(f"Апостеріорна оцінка похибки: {aposteriori_iteration}")

if __name__ == "__main__":
    main()
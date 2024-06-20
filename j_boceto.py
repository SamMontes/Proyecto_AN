import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import cumtrapz

# Paso 1: Definir la función c(x) y su inversa 1/c(x)
def c(x):
    return x + 1  # Ejemplo de una función c(x)

def inverse(g, domain, resolution=101):
    x = np.linspace(domain[0], domain[1], resolution)
    y = g(x)
    g_inverse = interp1d(y, x, fill_value="extrapolate")
    return g_inverse

# Paso 2: Calcular C(x) mediante integración numérica
def C(x, c_func, N=1000):
    x_vals = np.linspace(0, x, N)
    c_vals = 1 / c_func(x_vals)
    integral_vals = cumtrapz(c_vals, x_vals, initial=0)
    return integral_vals[-1]

# Paso 3: Calcular la inversa C^-1(x) usando interpolación lineal
def C_inverse(C_func, domain, resolution=101):
    x_vals = np.linspace(domain[0], domain[1], resolution)
    C_vals = np.array([C(x, c) for x in x_vals])
    C_inv_func = interp1d(C_vals, x_vals, fill_value="extrapolate")
    return C_inv_func

# Función para calcular la solución exacta I(C^-1(C(x) - t))
def I(x):
    return np.sin(x)  # Ejemplo de una función I(x)

def exact_solution(x, t, c_func, I_func):
    C_x = C(x, c_func)
    C_inv = C_inverse(lambda x: C(x, c_func), [0, 10])
    return I_func(C_inv(C_x - t))

# Función final: u_exact_variable_c
def u_exact_variable_c(x, n, c_func, I_func):
    t = n  # Suponiendo t = n para simplificación
    return exact_solution(x, t, c_func, I_func)

# Ejemplo de uso
x = 5
n = 2
result = u_exact_variable_c(x, n, c, I)
print(f"u_exact_variable_c({x}, {n}, c, I) = {result}")

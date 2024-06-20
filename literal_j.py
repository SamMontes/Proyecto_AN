#Funcion para calcular C(ξ) y C^-1(x), para cualquier X.
#Con las 2 funciones anteriores calcular I(C^-1(C(x)-t))
#Usar funcion u_exact_variable_c(x, n, c, I) que devuelva el anterior valor
import numpy as np
from scipy.interpolate import interp1d


#Definiendo la funcion a integrar
def c(t):
    #return 1/t (Como arreglo que no sea infinito?)
    return np.exp(1)**t**2
    

def calculate_C(x, n):
    #USANDO INTEGRACION POR EL METODO DEL TRAPECIO
    
    #Lista que tendra los distintos Xi
    xi_list = np.linspace(0, x, n+1)
    
    #Calculando el ancho del trapecio
    C = (x-0)/n
    
    #Usando la ecuacion general del trapecio, para calcular la integral
    resultado = (C/2)* (c(xi_list[0]) + 2*np.sum(c(xi_list[1:-1])) + c(xi_list[-1]))
    return resultado


def inverse(g, domain, n):
    #Lista con los valores obtenidos en C(x)
    x = np.linspace(domain[0], domain[1], n+1)
    
    #Evaluando la los valores de C(x)
    y = np.array([g(xi, n) for xi in x])
    
    #Usando interpolacion lineal para obtener la inversa de la funcion
    g_inverse = interp1d(y, x, kind="linear")
    return g_inverse


#Calculando C(ξ) con un numero de intervalo n
show_C = calculate_C(1, 5)
inverse_C = inverse(calculate_C, [0,1], 5)
show_inverse = inverse_C(show_C)

print(f"Funcion: {show_inverse:.7}")
print(f"Funcion: {show_C:.7}, Inversa: {show_inverse:.7}")

#FUNCION PRINCIPAL
def u_exact_variable_c(x, n, c, I):
    
   return True


#u_exact_variable_c()
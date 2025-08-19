import sympy as sp
import re

# -----------------------------
# FUNCIONES DE DIFERENCIAS CENTRADAS
# -----------------------------

def derivada_centrada_2p(fx, h):
    """Aproximación de la derivada primera usando diferencias centradas (2 puntos)."""
    return (fx[2] - fx[0]) / (2 * h)

def derivada_centrada_4p(fx, h):
    """Aproximación de la derivada primera usando diferencias centradas (4 puntos)."""
    return (-fx[4] + 8 * fx[3] - 8 * fx[1] + fx[0]) / (12 * h)

def segunda_derivada_centrada_2p(fx, h):
    """Aproximación de la derivada segunda usando diferencias centradas (2 puntos)."""
    return (fx[2] - 2 * fx[1] + fx[0]) / (h ** 2)

def segunda_derivada_centrada_4p(fx, h):
    """Aproximación de la derivada segunda usando diferencias centradas (4 puntos)."""
    return (-fx[4] + 16 * fx[3] - 30 * fx[2] + 16 * fx[1] - fx[0]) / (12 * h ** 2)

# -----------------------------
# FUNCIÓN AUXILIAR
# -----------------------------

def corregir_sintaxis(funcion_str):
    """
    Corrige la sintaxis de la función ingresada por el usuario.
    - Reemplaza 'sen' por 'sin' y 'e**x' por 'exp(x)'.
    - Agrega el operador '*' entre números y variables.
    """
    funcion_str = funcion_str.replace("sen", "sin").replace("e**x", "exp(x)").replace("e**", "exp")
    funcion_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', funcion_str)
    return funcion_str

def calcular_derivadas(funcion_str, x0, h):
    """
    Calcula la derivada simbólica y numérica de una función en un punto dado.
    """
    funcion_str = corregir_sintaxis(funcion_str)    
    x = sp.Symbol('x')
    
    try:
        funcion = sp.sympify(funcion_str, evaluate=True)
        derivada_simbolica = sp.diff(funcion, x)
        df_real = sp.lambdify(x, derivada_simbolica, modules="sympy")
        derivada_real = df_real(x0)
        f = sp.lambdify(x, funcion, modules="sympy")
        derivada_numerica = (f(x0 + h) - f(x0 - h)) / (2 * h)
        
        error_porcentaje = abs((derivada_numerica - derivada_real) / derivada_real) * 100
        
        print("\n" + "-"*50)
        print("Resultados de la derivada:")
        print("-"*50)
        print(f"Función derivada: {str(derivada_simbolica)}")
        print(f"Función derivada evaluada en x = {x0}: {str(derivada_numerica)}")
        print(f"Función derivada real en x = {x0}: {str(derivada_real)}")
        print("-"*50)
        print(f"Error porcentual: {error_porcentaje:.2f}%")
        print("-"*50)
    except Exception as e:
        print(f"Error al procesar la función: {e}")

print("-"*50)
funcion_str = input("Ingrese la función f(x): ")
x0 = float(input("Ingrese el valor de x donde calcular la derivada: "))
h = float(input("Ingrese el valor de h (valor de paso): "))

calcular_derivadas(funcion_str, x0, h)
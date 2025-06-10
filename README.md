# Proyecto de Análisis Numérico

## Descripción

Este proyecto implementa métodos de análisis numérico para calcular derivadas de funciones matemáticas en puntos específicos. Permite al usuario ingresar una función, un valor de `x` donde se desea calcular la derivada, y un valor de paso `h`. El programa utiliza la biblioteca `sympy` para cálculos simbólicos, `numpy` para cálculos numéricos, y `matplotlib` para la visualización gráfica de las funciones y sus derivadas, mostrando resultados precisos y el error porcentual.

## Características

- **Entrada de funciones matemáticas**: El usuario puede ingresar funciones matemáticas comunes como exponenciales (`e**x`), trigonométricas (`sin(x)`, `cos(x)`), logarítmicas (`log(x)`), polinomios, entre otras, que serán interpretadas correctamente.
- **Cálculo de derivadas**:
  - Derivada simbólica utilizando métodos algebraicos.
  - Derivada numérica utilizando diferencias finitas.
  - Derivada evaluada en un punto específico.
- **Manejo de errores**: El programa calcula el error porcentual entre la derivada numérica y la derivada simbólica para evaluar la precisión del cálculo.
- **Formato de salida**: Los resultados se muestran en un formato claro y legible, adaptando las expresiones matemáticas para facilitar su interpretación.

## Requisitos

- Python 3.6 o superior.
- Biblioteca `numpy`, `sympy`,`matplotlib`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone git@github.com:CandelaGonzalezP/analisis_numerico.git
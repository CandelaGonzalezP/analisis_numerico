# Proyecto de Análisis Numérico

Este proyecto fue desarrollado como parte de la materia **Análisis Numérico** de la carrera Ingeniería en Informática.  
Por **Candela González Privitera** y **Melina Gomez Torres**.

## Descripción

Este proyecto implementa el **método de diferencias centradas** para aproximar la primera y la segunda derivada de funciones matemáticas en un punto dado.  
El usuario puede ingresar la función, el valor de `x` en el cual desea evaluar, y el valor del paso `h`.  
El programa utiliza **Sympy** para cálculos simbólicos, **Numpy** para cálculos numéricos y maneja correcciones básicas de sintaxis en la entrada del usuario.

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
- Biblioteca `sympy`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone git@github.com:CandelaGonzalezP/analisis_numerico.git

## Referencias

- Chapra, S. C. & Canale, R. P. *Métodos numéricos para ingenieros*, McGraw-Hill, 2007.  
- Burden, R. L. & Faires, J. D. *Métodos numéricos*, Thomson, 2002.  
- Gerald, C. F. & Wheatley, P. O. *Análisis numérico con aplicaciones*, Prentice Hall, 2000.
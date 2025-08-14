import unittest
import math
import sympy as sp
from io import StringIO
from unittest.mock import patch
import project  # Tu archivo de código

class TestDerivadas(unittest.TestCase):

    def test_derivada_centrada_2p_lineal(self):
        # f(x) = 3x → derivada exacta = 3
        h = 0.001
        fx = [3*(1-h), 3*1, 3*(1+h)]
        self.assertAlmostEqual(project.derivada_centrada_2p(fx, h), 3, places=5)

    def test_derivada_centrada_4p_cuadratica(self):
        # f(x) = x² → derivada exacta en x=2 → 4
        h = 0.001
        x = 2
        fx = [ (x - 2*h)**2, (x - h)**2, x**2, (x + h)**2, (x + 2*h)**2 ]
        self.assertAlmostEqual(project.derivada_centrada_4p(fx, h), 4, places=5)

    def test_segunda_derivada_centrada_2p(self):
        # f(x) = x² → segunda derivada exacta = 2
        h = 0.001
        x = 3
        fx = [ (x - h)**2, x**2, (x + h)**2 ]
        self.assertAlmostEqual(project.segunda_derivada_centrada_2p(fx, h), 2, places=5)

    def test_segunda_derivada_centrada_4p(self):
        # f(x) = cos(x) → segunda derivada = -cos(x)
        h = 0.001
        x = math.pi / 4
        fx = [
            math.cos(x - 2*h),
            math.cos(x - h),
            math.cos(x),
            math.cos(x + h),
            math.cos(x + 2*h)
        ]
        esperado = -math.cos(x)
        self.assertAlmostEqual(project.segunda_derivada_centrada_4p(fx, h), esperado, places=5)

    def test_corregir_sintaxis(self):
        entrada = "3sen(x)+2e**x"
        salida = project.corregir_sintaxis(entrada)
        self.assertEqual(salida, "3*sin(x)+2*exp(x)")

    @patch("builtins.input", side_effect=["x**2", "3", "0.001"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_calcular_derivadas_completo(self, mock_stdout, mock_input):
        project.calcular_derivadas("x**2", 3, 0.001)
        salida = mock_stdout.getvalue()
        self.assertIn("Función derivada: 2*x", salida)
        self.assertIn("Error porcentual: 0.00%", salida)
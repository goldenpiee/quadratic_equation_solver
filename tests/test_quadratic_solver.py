import unittest
from src.quadratic_solver import solve_quadratic_equation

class TestQuadraticSolver(unittest.TestCase):

    def test_real_roots(self):
        self.assertEqual(solve_quadratic_equation(1, -3, 2), (2, 1))

    def test_complex_roots(self):
        self.assertEqual(solve_quadratic_equation(1, 1, 1), ((-0.5 + 1j * 0.866), (-0.5 - 1j * 0.866)))

    def test_zero_discriminant(self):
        self.assertEqual(solve_quadratic_equation(1, -2, 1), (1, 1))

if __name__ == '__main__':
    unittest.main()

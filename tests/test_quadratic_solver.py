import unittest
from src.quadratic_solver import solve_quadratic_equation

class TestQuadraticSolver(unittest.TestCase):

    def test_real_roots_zero_discriminant(self):
        result = solve_quadratic_equation(1, -2, 1)
        self.assertEqual(result, (1, 1))
        print(f"Test case 'test_real_roots_zero_discriminant' result: {result}")

    def test_real_roots_positive_discriminant(self):
        result = solve_quadratic_equation(1, -3, 2)
        self.assertEqual(result, (2, 1))
        print(f"Test case 'test_real_roots_positive_discriminant' result: {result}")

    def test_real_roots_negative_discriminant(self):
        result = solve_quadratic_equation(1, 1, 1)
        self.assertEqual(result, None)
        print(f"Test case 'test_real_roots_negative_discriminant' result: {result}")

if __name__ == '__main__':
    unittest.main()

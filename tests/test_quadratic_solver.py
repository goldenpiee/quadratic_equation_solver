import unittest
from src.quadratic_solver import solve_quadratic_equation


class TestQuadraticSolver(unittest.TestCase):

    def test_real_roots_zero_discriminant(self):
        self.assertEqual(solve_quadratic_equation(1, -2, 1), (1, 1))

    def test_real_roots_positive_discriminant(self):
        self.assertEqual(solve_quadratic_equation(1, -3, 2), (2, 1))

    def test_real_roots_negative_discriminant(self):
        self.assertEqual(solve_quadratic_equation(1, 1, 1), None)

    def test_a_zero(self):
        with self.assertRaises(ValueError):
            solve_quadratic_equation(0, 2, 3)

    def test_a_and_b_zero(self):
        with self.assertRaises(ValueError):
            solve_quadratic_equation(0, 0, 3)


if __name__ == '__main__':
    unittest.main()

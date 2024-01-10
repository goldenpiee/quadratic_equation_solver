# Quadratic Equation Solver

Этот проект предоставляет простую функцию для вычисления корней квадратного уравнения.

## Использование

```python
from src.quadratic_solver import solve_quadratic_equation

# Пример использования
roots = solve_quadratic_equation(1, -3, 2)
print("Корни уравнения:", roots)
```
## Установка
```bash
pip install -r requirements.txt
```
## Тестирование
```bash
python -m unittest discover -s tests -p 'test_*.py'
```
## Оценка покрытия кода
```bash
coverage run -m unittest discover -s tests -p 'test_*.py'
coverage report
```
[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=goldenpiee_quadratic_equation_solver)](https://sonarcloud.io/summary/new_code?id=goldenpiee_quadratic_equation_solver)

[![Coverage Status](https://coveralls.io/repos/github/goldenpiee/quadratic_equation_solver/badge.svg?branch=main)](https://coveralls.io/github/goldenpiee/quadratic_equation_solver?branch=main)


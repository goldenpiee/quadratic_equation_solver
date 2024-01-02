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
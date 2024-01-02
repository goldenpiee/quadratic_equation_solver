def solve_quadratic_equation(a, b, c):
    # Вычисляем дискриминант
    discriminant = b ** 2 - 4 * a * c

    # Проверяем значение дискриминанта
    if discriminant >= 0:
        # Вычисляем корни для действительных чисел
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return root1, root2
    else:
        # Для отрицательного дискриминанта возвращаем None
        return None

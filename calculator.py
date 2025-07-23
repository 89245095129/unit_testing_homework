
def calculator(a, b, operation):
    """
    Выполняет базовые арифметические операции над двумя числами.
    
    Аргументы:
        a (int/float): Первое число
        b (int/float): Второе число
        operation (str): Операция ('add', 'subtract', 'multiply', 'divide')
    
    Возвращает:
        int/float: Результат операции
        
    Исключения:
        ValueError: Если передана неизвестная операция
        ZeroDivisionError: При делении на ноль
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Unknown operation")


def is_even(num):
    """
    Проверяет, является ли число четным.
    
    Аргументы:
        num (int): Число для проверки
    
    Возвращает:
        bool: True если число четное, иначе False
    """
    return num % 2 == 0


def safe_divide(a, b):
    """
    Безопасное деление двух чисел с обработкой деления на ноль.
    
    Аргументы:
        a (int/float): Делимое
        b (int/float): Делитель
    
    Возвращает:
        float: Результат деления a на b
        
    Исключения:
        ZeroDivisionError: Если делитель равен нулю
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
    
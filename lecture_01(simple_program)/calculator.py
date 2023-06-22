def add(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both x and y must be numeric values.")
    return x + y

def subtract(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both x and y must be numeric values.")
    return x - y

def multiply(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both x and y must be numeric values.")
    return x * y

def divide(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both x and y must be numeric values.")
    if y == 0:
        raise ValueError("can't divide by zero")
    return x / y
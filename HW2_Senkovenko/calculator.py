def addition(val1, val2):
    return val1 + val2

def multiplication(val1, val2):
    return val1 * val2

def div(val1, val2):
    if val2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return val1 / val2

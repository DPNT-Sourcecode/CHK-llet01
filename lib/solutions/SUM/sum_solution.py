# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("x and y should be integers")
    if x < 0 or x > 100:
        raise ValueError("x should be between 0 and 100")
    if y < 0 or y > 100:
        raise ValueError("x should be between 0 and 100")
    return x + y


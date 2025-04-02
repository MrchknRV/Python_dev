def map(function, items):
    """Собственная реализация встроенной функции map"""
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    """Собственная реализация встроенной функции filter"""
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

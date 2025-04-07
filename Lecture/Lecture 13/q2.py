def safe_calculate(num):
    # handle the error
    try:
        return calculate(num)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return None

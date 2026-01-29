from functools import wraps
def my_decorator(func):
    @wraps(func)
    def loger (a,b):
        print("Function:",func.__name__)
        print("Arguments:",a,b)
        print("Result:",func(a,b))
    return loger

@my_decorator
def multiply(a, b):
    return a*b

multiply(3,4)
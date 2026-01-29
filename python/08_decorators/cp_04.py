from functools import wraps
def my_decorator (func):
    @wraps(func)
    def uppercase_decorator():
        upper = func()
        return upper.upper()
    return uppercase_decorator

@my_decorator
def message():
    return "hello world"

print("result: ",message())

# def my_decorator (func):
#     def uppercase_decorator():
#         upper = func()
#         print("result: ",upper.upper())
#     return uppercase_decorator

# @my_decorator
# def message():
#     return "hello world"

# message()
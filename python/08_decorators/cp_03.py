from functools import wraps
def my_decorator(func):
    @wraps(func)
    def mult_two(x,y):
        multi =func(x,y)
        return multi*2
    return mult_two

@my_decorator 
def add (a,b):
    return a+b
print ("result: ",add(3,4))
def my_decorator(func):
    def good_bay():
        func()
        print("Goodbye!")
    return good_bay

@my_decorator
def greet ():
    print("hello function")

greet()
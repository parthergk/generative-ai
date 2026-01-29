from functools import wraps
def my_decorator(func):
    @wraps(func)
    def check_login(type):
        if type=="admin":
            func()
        else:
            print("Access Denied")
    return check_login

@my_decorator
def view_dashboard():
    print("Welcome to dashboard")

view_dashboard("not admin")
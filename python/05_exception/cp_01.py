try:
    result = 10/0
except ZeroDivisionError :
    print(f"not devided by 0")

class PostiveNumber(Exception):
    pass

def rais_fun():
    check_number = -12
    if check_number < 0:
        raise PostiveNumber("Enter a postive value")

try:
    rais_fun()
except PostiveNumber as err:
    print(err)
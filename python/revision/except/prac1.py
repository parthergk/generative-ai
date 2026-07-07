try:
    print("A")
    print(10 / 2)
    print("B")

except:
    print("Error")

try:
    print("A")
    print(10 / 0)
    print("B")

except:
    print("Error")

print("Done")

try:
    print(10 / 0)

except Exception:
    print("General Error")

except ZeroDivisionError:
    print("Divide Error")

try:
    print("A")

except:
    print("Error")

else:
    print("Success")
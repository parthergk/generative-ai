class Yadxy:
    teacher = "rahul"
    student = "raman"

yadxy_obj = Yadxy()
print(f"teacher name: {yadxy_obj.teacher}")

yadxy_obj.teacher = "gauarv"
print(f"teacher name after change: {yadxy_obj.teacher}")

del yadxy_obj.teacher
print(f"teacher name after delete: {yadxy_obj.teacher}")

yadxy_obj.fee = "paid"
print(f"new attribute: {yadxy_obj.fee}")

del yadxy_obj.fee
print(f"after deleting fee: {yadxy_obj.fee}")
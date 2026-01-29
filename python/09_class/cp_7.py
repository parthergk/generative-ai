class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "A: Herbal blend"

class D(C, B):
    pass

mro = D()

print(mro.label)
# print(D.__mro__)
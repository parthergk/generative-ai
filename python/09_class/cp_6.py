class Yadxy:
    def __init__(self, type_, no):
        self.type = type_
        self.no = no


class Medic(Yadxy):
    def __init__(self, type_, no, launch):
        super().__init__(type_, no)
        self.launch= launch

    def addType(self):
        print(f"Type of yadxy", self.type, "launched when", self.launch)


obj_Medic = Medic("B2B", 1, "not_fixed")
obj_Medic.addType()

obj_Yadxy = Yadxy("B2C", 1)

print(f"From yadxy", obj_Yadxy.type)

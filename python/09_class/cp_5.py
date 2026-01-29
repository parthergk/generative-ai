class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepair(self):
        print(f"{self.type} chai is ready")

make_chai = BaseChai("adrak")
make_chai.prepair()

class NasediChai(BaseChai):
    def add_nase(self):
        print (f"adding {self.type} for nasedi chai")

make_nasedi_chai = NasediChai("ganja")
make_nasedi_chai.add_nase()
make_nasedi_chai.prepair()


class ChaiShop:
    chai_cls = BaseChai
    print(f"type fo chai_cls", type(chai_cls))

    def __init__(self):
        self.chai = self.chai_cls("ilaychi")
    def serve(self):
        print(f"type fo chai", type(self.chai))
        print(f"serving {self.chai.type} chai in shop")

shop_chai = ChaiShop()

shop_chai.chai.prepair()
shop_chai.serve()
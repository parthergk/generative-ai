class Tea:
    def __init__(self, type_, no):
        self.type = type_
        self.no = no
    
    @classmethod
    def from_dict(cls, orderType):
        return cls(orderType["tea_type"],orderType["size"])

    @classmethod
    def from_str(cls, typeString):
        tea_type, size = typeString.split("_")
        return cls(tea_type, size)
    
order1 = Tea.from_dict({"tea_type":"leamon", "size":"2" })

print(order1.__dict__)

order2 = Tea.from_str("hony_3")
print(order2)
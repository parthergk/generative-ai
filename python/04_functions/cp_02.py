chai_type = "balck"

def update_chai():
    chai_type = "green"
    def update_again():
        nonlocal chai_type
        chai_type = "milk"
        # print(f"Chai type inside update_chai:", chai_type)
    update_again()
    # print(f"Chai type inside update_chai:", chai_type)

update_chai()
print(f"Chai type inside update_chai:", chai_type)
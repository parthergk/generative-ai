def yadxy(item):
    try:
        print(f"Checking {item} type")
        if(item == "unknown"):
            raise ValueError("this item not valied")
    except ValueError as e:
        print (e)
    else:
        print("item type checked")
    finally :
        print("i will run always")

yadxy("saas")
yadxy("unknown")
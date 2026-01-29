class partherError(Exception):
    pass

def yadxy(item):
    if(item=="tea"):
        raise partherError("this item not assignebal")
    
yadxy("tea")
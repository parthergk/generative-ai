all_fruites = {
    "new": ["apple","orange","mango"],
    "old": ["banana", "papaya", "apple"]
}

all_uniqe_fruites = [fruites for type in all_fruites.values() for fruites in type if fruites != "apple"]

print(f"all uniqe fruites", all_uniqe_fruites)
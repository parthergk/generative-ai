def infinite_name():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refil = infinite_name()

for __ in range(5):
    print(f"infinite name", next(refil))
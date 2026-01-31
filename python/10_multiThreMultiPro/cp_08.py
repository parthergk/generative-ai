from multiprocessing import Process, Value

def fun(counter):
    for _ in range(10000):
        with counter.get_lock():
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)
    proc = [Process(target=fun, args=(counter, )) for _ in range (4)]
    [p.start() for p in proc]
    [p.join() for p in proc]

    print("final counter value ",counter.value)
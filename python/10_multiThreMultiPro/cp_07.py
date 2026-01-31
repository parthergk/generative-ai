from multiprocessing import Process, Queue

def fun(queue):
    queue.put("hey how are you")


if __name__ == "__main__":
    queue = Queue()
   
    pr = Process(target=fun, args=(queue, ))
    pr.start()
    pr.join()

    print(queue.get())
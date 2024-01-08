from multiprocessing import Queue

new_queue = Queue(maxsize=3)
new_queue.put(1)
print(new_queue.get())

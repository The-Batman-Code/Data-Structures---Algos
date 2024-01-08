import queue

new_queue = queue.Queue(maxsize=3)
print(new_queue.empty())
new_queue.put(1)
new_queue.put(2)
new_queue.put(3)
print(new_queue)
print(new_queue.empty())
print(new_queue.full())
print(new_queue.get())
print(new_queue.qsize())

from collections import deque

new_queue = deque(maxlen=3)
print(new_queue)

new_queue.append(1)
new_queue.append(2)
new_queue.append(3)

print(new_queue)
new_queue.append(4)
print(new_queue)
print(new_queue.popleft())
print(new_queue)
new_queue.clear()
print(new_queue)

import Queue as queue
import time

# prio_queue = queue.PriorityQueue()
# prio_queue.put((4, time.time(), 'super blah'))
# time.sleep(0.1)
# prio_queue.put((1, time.time(), 'This thing would come after Some Thing if we sorted by this text entry'))
# time.sleep(0.1)
# prio_queue.put((2, time.time(), 'Some thing'))
# time.sleep(0.1)
# prio_queue.put((3, time.time(), 'blah'))

# while not prio_queue.empty():
#     item = prio_queue.get()
#     print('%s.%s - %s' % item)



prio_queue = queue.PriorityQueue()
prio_queue.put((2, 8, 'super blah'))
prio_queue.put((1, 4, 'Some thing'))
prio_queue.put((1, 3, 'This thing would come after Some Thing if we sorted by this text entry'))
prio_queue.put((5, 1, 'blah'))

while not prio_queue.empty():
    item = prio_queue.get()
    print('%s.%s - %s' % item)
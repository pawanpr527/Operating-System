import threading
import time
import random
import queue

# Method 1 using Mutex
# buffer = []
# max_size = 5
# condition = threading.Condition()

# def producer():
#      for i in range(10):
#         item = f"item - {i}"
#         with condition:
#           while len(buffer) == max_size:
#                condition.wait()
          
#           buffer.append(item)
          
#           print(f"produce {item}")
          
#           condition.notify()
#         time.sleep(random.uniform(0.1,0.5))

# def consumer():
#     for i in range(10):
#         with condition:
#             while not buffer:
#                 condition.wait()
#             item = buffer.pop(0)
#             print(f"consumed : {item}")

#             condition.notify()
#         time.sleep(random.uniform(0.2,0.6))

# if __name__ == "__main__":
#     t0 = threading.Thread(target=producer)
#     t1 = threading.Thread(target=consumer)
#     t0.start()
#     t1.start()
#     t0.join()
#     t1.join()
#     print("all item processed")


# Using Queue


# buffer = queue.Queue(maxsize=5)

# def producer(pid):
#     for i in range(10):
#         item = f"Item - {i}"
#         buffer.put(item)
#         print(f"Produce {pid} : {item}")
#         time.sleep(random.uniform(0.1,0.5))
# def consumer(cid):
#     for i in range(10):
#         item = buffer.get()
#         print(f"Consumed {cid} : {item}")
#         time.sleep(random.uniform(0.2,0.6))
#         buffer.task_done()

# if __name__ == "__main__":
#     t0 = threading.Thread(target=producer)
#     t1 = threading.Thread(target=consumer)
#     t0.start()
#     t1.start()
#     t0.join()
#     t1.join()

# # for 2 producer and 2 consumer
# if __name__ == "__main__":
#     t0 = [threading.Thread(target=producer, args=(i,)) for i in range(3)]
#     t1 = [threading.Thread(target=consumer,args=(i,)) for i in range(3)]

#     for t in t0+t1:
#         t.start()
#     for t in t0+t1:
#         t.join()


##Using Semaphore

buffer = []
max_size = 5

empty = threading.Semaphore(max_size)  # track empty slots
full = threading.Semaphore(0)     # track filled slots
mutex = threading.Semaphore(1)    #ensure mutual exclusion

def producer(pid):
    for i in range(10):
        empty.acquire()

        mutex.acquire()

        buffer.append(i)
        print(f"Producer {pid} is producing {i}")

        mutex.release()

        full.release()  # send signal to consumer
        time.sleep(random.uniform(0.1,0.6))
def consumer(cid):
    for i in range(10):
        full.acquire()

        mutex.acquire()

        item = buffer.pop(0)

        print(f"Consumer {cid} is consuming {i}")

        mutex.release()

        empty.release()  # sends signal to empty that a empty slot is available
        time.sleep(random.uniform(0.2,0.7))
if __name__ == "__main__":
    t0 = [threading.Thread(target=producer,args=(i,)) for i in range(2)]
    t1 = [threading.Thread(target=consumer,args=(i,)) for i in range(2)]

    for t in t0+t1:
        t.start()
    for t in t0+t1:
        t.join()


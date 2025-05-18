# import threading
# import time 
# import random
# class DiningPhilospher:
#     def __init__(self,number_philosopher=5):
#         self.N = number_philosopher
#         self.fork = [threading.Semaphore(1) for _ in range(self.N) ]
#         self.butler = threading.Semaphore(self.N-1)
    
#     def wants_to_eat(self,philosoher_id):
#          left = philosoher_id
#          right = (philosoher_id+1) % self.N
        
#          print(f"Philosopher {philosoher_id} is thinking ")
#          time.sleep(1)

#          self.butler.acquire()
#          print(f"philosopher {philosoher_id} is hungry")
         
#          if philosoher_id%2==0:

#            self.fork[left].acquire()
#            print(f"Philosopher {philosoher_id} picked up left fork {left}")

#            self.fork[right].acquire()
#            print(f"Philosopher {philosoher_id} picked up right fork {right}")
        
#          else:
#              self.fork[right].acquire()
#              print(f"Philosopher {philosoher_id} picked up right fork {right}")
     
#              self.fork[left].acquire()
#              print(f"Philosopher {philosoher_id} picked up left fork {left}")

#          print(f"Philosopher {philosoher_id} is eating")
#          time.sleep(1)
#          self.fork[left].release()
#          self.fork[right].release()
#          print(f"Philosoper {philosoher_id} pick down fork")
#          self.butler.release()
    

# class Philosopher(threading.Thread):
#     def __init__(self,philosopher_id,table: DiningPhilospher):
#         super().__init__()
#         self.id = philosopher_id
#         self.table = table
    
#     def run(self):
#         self.table.wants_to_eat(self.id)
# if __name__ == "__main__":
#     num_of_philosopher = 10
#     table = DiningPhilospher(num_of_philosopher)
#     philosophers = [Philosopher(i,table) for i in range(num_of_philosopher)]

#     for p in philosophers:
#         p.start()
#     for p in philosophers:
#         p.join()

# Without using Classes 

import threading
import time

number_of_philosopher = 5
fork = [threading.Semaphore(1) for i in range(number_of_philosopher)]

def philosopher(pid):
    left = pid
    right = (pid+1)%number_of_philosopher
    
    for _ in range(3):
        print(f"philosopher {pid} is thinking")
        time.sleep(1)
        print(f"philosopher {pid} is hungry")
        if pid%2==0:
            fork[left].acquire()
            print(f"philosopher {pid} picks left fork {left}")
            fork[right].acquire()
            print(f"philosopher {pid} pick right fork {right}")
        else:
            fork[right].acquire()
            print(f"philosopher {pid} pick right fork {right}")
            fork[left].acquire()
            print(f"philosopher {pid} picks left fork {left}")
        print(f"philosopher {pid} is eating")
        time.sleep(1)
        fork[left].release()
        fork[right].release()
        print(f"philosopher {pid} puts down fork")
        

if __name__ == "__main__":
    philosophers = [threading.Thread(target=philosopher,args=(i,)) for i in range(number_of_philosopher)]
    
    for p in philosophers:
        p.start()
    for p in philosophers:
        p.join()
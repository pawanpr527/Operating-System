import threading 
import time

share_counter = 0

class Peterson:
    def __init__(self):
        self.flag= [False,False]
        self.turn = 0
        self.lock = threading.Lock()
    
    def acquire(self,thread_id):
        other = 1-thread_id
        with self.lock:
            self.flag[thread_id] = True
            self.turn = other
        
        while self.flag[other] and self.turn == other:
            time.sleep(1)
            print(f"{self.turn} process is waiting")
    
    def release(self,thread_id):
        with self.lock:
          self.flag[thread_id] = False

def worker(plock,thread_id):
    global share_counter
    for _ in range(1000):
        plock.acquire(thread_id) 

 # for each iteration both thread is increment by one. So per one iteration increment share counter by 2 (t0+t1)
        
        share_counter+=1

        plock.release(thread_id)
    
if __name__ == "__main__":
    plock = Peterson()

    t0 = threading.Thread(target=worker,args=(plock,0))
    t1 = threading.Thread(target=worker,args=(plock,1))

    t0.start()
    t1.start()
    t0.join()
    t1.join()
    
    print(f"share counter is {share_counter}")
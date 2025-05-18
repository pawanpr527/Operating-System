import threading 
import time

class ReaderWriter:
    def __init__(self):
        self.read_count = 0
        self.mutex = threading.Lock()
        self.wrt = threading.Semaphore(1)
    
    def reader(self,reader_id):
        
        #all thread of reader first execute by first acquire then they go to other acquire
        '''so all reader threads first enters in mutex.acquire and execute one by one with increment 
        when all thread executes they all reader thread moves in another acquire and 
        decrement read count 1 by each thread
'''
        self.mutex.acquire()

        self.read_count+=1
        if self.read_count==1:   # First reader 
            self.wrt.acquire()
        self.mutex.release()    
        print(f"{reader_id} reading")
        time.sleep(1)
        
        self.mutex.acquire()
        self.read_count-=1
        if self.read_count==0:
            self.wrt.release()   # Last reader realease lock on writer
        self.mutex.release()
    
    def writer(self,writer_id):
      try:
         self.wrt.acquire()
         print(f"{writer_id} is writing")
         time.sleep(1)
         self.wrt.release()
        
      except RuntimeError:
         print("Conflict")
if __name__ == "__main__":
   rw = ReaderWriter()
   reader = []
   writer = []
   
   for i in range(10):
      r = threading.Thread(target=rw.reader,args=(i+1,))
      w = threading.Thread(target=rw.writer,args=(i+1,))
      reader.append(r)
      writer.append(w)
   for r,w in zip(reader,writer):
      r.start()
      w.start()
   for r,w in zip(reader,writer):
      r.join()
      w.join()
  
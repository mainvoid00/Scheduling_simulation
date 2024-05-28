import time
import queue
from tabulate import tabulate



#FCFS, SJF, 비선점 Priority, 선점 Priority, RR, SRT, HRN



class Scheduling() :
    burst_time=[]
    priority=[]
    arrival_time=[]
    PID=[]
    ready_queue=[]
    DISPATCH=False
    def __init__(self, arrival_time, burst_time ,PID, priority):
        self.burst_time = (burst_time)
        self.arrival_time =(arrival_time)
        self.priority= (priority)
        self.PID = PID
  
    def Print(self):
        print("-----Process Information-----")

        headers = ['PID', 'Arrival time', 'Burst time', 'Priority']

        data = [[0 for _ in range(4)] for _ in range(len(self.PID))]


        for i in range(len(self.PID)):
            data [i][0] = self.PID[i]
            data [i][1] = self.arrival_time[i]
            data [i][2] = self.burst_time[i]
            data [i][3] = self.priority[i]

        print(tabulate(data, headers, tablefmt='fancy_grid'))

def init(arrival_time, burst_time, PID, priority):
    
    with open("./init.txt", 'r') as f :
        liens=[]
        PID_INDEX=0
        while True:
            line = f.readline()
            if not line:
                break
                
            data= line.split(' ')
            
            PID.append(PID_INDEX)
            PID_INDEX+=1
            burst_time.append(int(data[1]))
            arrival_time.append(int(data[0]))
            priority.append(int(data[2]))
            
            
''' Process information SORT'''
def swap(arrival_time, burst_time, priority):
    for i in range(len(arrival_time)-1):
        for j in range(i+1, len(arrival_time)):
            if arrival_time[i] > arrival_time[j]:
                temp_arrival_time = arrival_time[i]
                temp_burst_time = burst_time[i]
                temp_priority = priority[i]
                
                arrival_time[i] = arrival_time[j]
                burst_time[i] = burst_time[j]
                priority[i] = priority[j]
                
                arrival_time[j] = temp_arrival_time
                burst_time[j] = temp_burst_time
                priority[j] = temp_priority
        
                
        
            
class FCFS(Scheduling):
     
    def __init__(self, arrival_time, burst_time, PID, priority):
        super().__init__(arrival_time, burst_time, PID, priority)
        self.st = time.time()
        self.pid_index = 0
        self.ready_queue = []
        
    
    
    
    
    def run(self):

        print("-----FCFS START-----")
        
        while True:
            now = time.time()
            print("now time=",int(now - self.st))
            if self.pid_index < len(self.arrival_time) and int(now - self.st) >= self.arrival_time[self.pid_index]:
                self.ready_queue.append(self.PID[self.pid_index])
                print("PID", self.PID[self.pid_index], "enqueue")
                self.pid_index += 1
            
            print("ready_queue =", self.ready_queue)
            
            if self.DISPATCH == False and len(self.ready_queue) >0:
                self.DISPATCH= True
                dispatch_pid= self.ready_queue.pop(0)
                dispatch_st = now

                
                
                
                
            if self.DISPATCH == True:
                
                print("running pid=", dispatch_pid, "burst time=", int(now-dispatch_st) )
                if(int(self.burst_time[dispatch_pid]-int(now-dispatch_st)) == 0):
                    print("time out PID",dispatch_pid)
                    self.DISPATCH = False
                    if len(self.ready_queue) > 0:
                        self.DISPATCH= True
                        dispatch_pid= self.ready_queue.pop(0)
                        dispatch_st = now  

                    
                
                
            if(len(self.ready_queue)== 0 and self.DISPATCH == False):
                break
            
            
            
            
            time.sleep(1)
            

        
        
    
    
            
            
        

def main():
    burst_time=[]
    arrival_time=[]
    PID=[]
    priority=[]
    init(arrival_time, burst_time, PID, priority)
    swap(arrival_time, burst_time, priority)
    
    
    
    scheduling_fcfs = FCFS(arrival_time, burst_time, PID, priority)
    scheduling_fcfs.Print()
    scheduling_fcfs.run()
    




    
    
    
    
    
    


if __name__ == "__main__":
    main()


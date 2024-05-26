import time
import queue
#FCFS, SJF, 비선점 Priority, 선점 Priority, RR, SRT, HRN



class Scheduling() :
    burst_time=[]
    priority=[]
    arrival_time=[]
    PID=[]
    ready_queue=[]
    def __init__(self, arrival_time, burst_time ,PID, priority):
        self.burst_time = (burst_time)
        self.arrival_time =(arrival_time)
        self.priority= (priority)
        self.PID = PID
'''        
    def Print(self):
        print(self.PID[0], self.arrival_time[0], self.burst_time[0])
        print(self.PID[1], self.arrival_time[1], self.burst_time[1])
        print(self.PID[2], self.arrival_time[2], self.burst_time[2])
'''

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
            burst_time.append(data[1])
            arrival_time.append(data[0])
            priority.append(data[2])
            
            
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
    print("-----FCFS START-----")
   
    
    
    def run(self):
         st=time.time()
         pid_index=0
         while True:
        
            now= time.time()
            print((now - st))
            if int(now) == arrival_time[pid_index] :
                ready_queue.append(pid[pid_index])
                print("PID",PID[pid_index],"enqueue")
                pid_index+=1
            
            print("ready_queue = ", ready_queue)
            
            time.sleep(1)
        
        
    
    
            
            
        

def main():
    burst_time=[]
    arrival_time=[]
    PID=[]
    priority=[]
    init(arrival_time, burst_time, PID, priority)
    swap(arrival_time, burst_time, priority)
    
    
    
    scheduling_fcfs = FCFS(arrival_time, burst_time, PID, priority)
    #scheduling_fcfs.Print()
    scheduling_fcfs.run()
    
    
    
    
    
    


if __name__ == "__main__":
    main()


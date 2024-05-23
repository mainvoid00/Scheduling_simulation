import time

#FCFS, SJF, 비선점 Priority, 선점 Priority, RR, SRT, HRN



class Scheduling() :
    burst_time=[]
    priority=[]
    arrival_time=[]
    PID=[]
    
    def __init__(self, burst_time, arrival_time, PID, priority):
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.priority= priority
        self.PID = PID
        
    def Print(self):
        print(self.PID[0], slef.PID[1])


def init(burst_time, arrival_time, PID, priority):
    
    with open("./init.txt", 'r') as f :
        liens=[]
        while True:
            line = f.readline()
            if not line:
                break
                
            data= line.split(' ')
            
            PID.append(data[0])
            burst_time.append(data[1])
            arrival_time.append(data[2])
            priority.append(data[3])
            
            
            
            
def FCFS(Scheduling):
    pass
            
            
            
        
        

'''
def FCFS():
    pass

def SJF():
    pass

def Priority_Preemptive():
    pass

def Priority_Nonpreemptive():
    pass

'''

def main():
    burst_time=[]
    arrival_time=[]
    PID=[]
    priority=[]
    init(burst_time, arrival_time, PID, priority)
    
    scheduling = Scheduling(burst_time, arrival_time, PID, priority)
    
    
    
    
    
    


if __name__ == "__main__":
    main()


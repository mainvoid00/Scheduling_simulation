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
        print(self.PID[0], self.PID[1])


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
            
            
            
            
class FCFS(Scheduling):
     
    def __init__(self, burst_time, arrival_time, PID, priority):
        super().__init__(burst_time, arrival_time, PID, priority)

    n = len(self.PID)
    processes = sorted(zip(self.arrival_time, self.burst_time, self.PID), key=lambda x: x[0])
        
    current_time = 0
    waiting_time = []
    turnaround_time = []
        
    for arrival, burst, pid in processes:
        if current_time < arrival:
                current_time = arrival
        start_time = current_time
        finish_time = start_time + burst
        current_time = finish_time
        waiting_time.append(start_time - arrival)
        turnaround_time.append(finish_time - arrival)
        
    for i, (arrival, burst, pid) in enumerate(processes):
            print(f"PID: {pid}, 도착 시간: {arrival}, 실행 시간: {burst}, 대기 시간: {waiting_time[i]}, 반환 시간: {turnaround_time[i]}")
        
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
        
    print(f"평균 대기 시간: {avg_waiting_time}")
    print(f"평균 반환 시간: {avg_turnaround_time}")
            
            
        

def main():
    burst_time=[]
    arrival_time=[]
    PID=[]
    priority=[]
    init(burst_time, arrival_time, PID, priority)
    
    scheduling_fcfs = FCFS(burst_time, arrival_time, PID, priority)
    scheduling_fcfs.Print()
    scheduling_fcfs.schedule()
    
    
    
    
    


if __name__ == "__main__":
    main()


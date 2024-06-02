import time
import queue
from tabulate import tabulate
import matplotlib.pyplot as plt
import pandas as pd

class Process:
    
    def __init__(self, burst_time, priority, arrival_time, PID):
        self.burst_time = burst_time
        self.priority = priority
        self.arrival_time = arrival_time
        self.PID = PID
        self.wait_start_time = []
        self.wait_end_time = []
        self.burst_start_time = []
        self.burst_end_time = []
        self.wait_time =0
        self.turn_around_time= 0
        
class Scheduling:
    def __init__(self, arrival_time, burst_time, PID, priority):
        self.ready_queue = []
        self.process = []
        self.DISPATCH = False
        self.PID = PID  # PID 리스트를 인스턴스 변수로 추가
        for i in range(len(PID)):
            self.process.append(Process(burst_time[i], priority[i], arrival_time[i], PID[i]))

    def Print(self):
        print("-----Process Information-----")
        headers = ['PID', 'Arrival time', 'Burst time', 'Priority']
        data = [[0 for _ in range(4)] for _ in range(len(self.PID))]
        for i in range(len(self.PID)):
            data[i][0] = self.process[i].PID
            data[i][1] = self.process[i].arrival_time
            data[i][2] = self.process[i].burst_time
            data[i][3] = self.process[i].priority
        print(tabulate(data, headers, tablefmt='fancy_grid'))

def init(arrival_time, burst_time, PID, priority):
    with open("./init.txt", 'r') as f:
        PID_INDEX = 0
        while True:
            line = f.readline()
            if not line:
                break
            data = line.split(' ')
            PID.append(PID_INDEX)
            PID_INDEX += 1
            burst_time.append(int(data[1]))
            arrival_time.append(int(data[0]))
            priority.append(int(data[2]))

def swap(arrival_time, burst_time, priority):
    for i in range(len(arrival_time) - 1):
        for j in range(i + 1, len(arrival_time)):
            if arrival_time[i] > arrival_time[j]:
                arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
                burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
                priority[i], priority[j] = priority[j], priority[i]

class FCFS(Scheduling):
    def __init__(self, arrival_time, burst_time, PID, priority):
        super().__init__(arrival_time, burst_time, PID, priority)

    def Run(self):
        print("----------FCFS START----------")
        flag = True
        run_time = 0
        pid_count = 0
        while flag:
            
            # Ready queue Enqueue
            if pid_count < len(self.process) and self.process[pid_count].arrival_time == run_time:
                self.ready_queue.append(self.process[pid_count].PID)
                self.process[pid_count].wait_start_time.append(run_time)
                print("------------------------------")
                print("PID", self.process[pid_count].PID, "enqueue now time =", run_time)
                print("ready_queue =", self.ready_queue)
                print("------------------------------")
                pid_count += 1

            # Dispatch
            if self.ready_queue and not self.DISPATCH:
                dispatch_start_time = run_time
                self.DISPATCH = True
                dispatch_pid = self.ready_queue.pop(0)
                print("------------------------------")
                print("dispatch = PID", dispatch_pid, "now time = ", run_time)
                print("------------------------------")
                self.process[dispatch_pid].wait_end_time.append(run_time)
                self.process[dispatch_pid].burst_start_time.append(run_time)

            # time out
            if self.DISPATCH:
                dispatch_pid = self.process[dispatch_pid].PID
                if int(self.process[dispatch_pid].burst_time - (run_time - dispatch_start_time)) == 0:
                    print("------------------------------")
                    print("time out PID", dispatch_pid, "now time = ",run_time)
                    print("------------------------------")
                    self.process[dispatch_pid].burst_end_time.append(run_time)
                    self.process[dispatch_pid].turn_around_time = run_time - self.process[dispatch_pid].arrival_time
                    self.DISPATCH = False
                    
                    
                    
            # Dispatch
            if self.ready_queue and not self.DISPATCH:
                
                dispatch_start_time = run_time
                self.DISPATCH = True
                dispatch_pid = self.ready_queue.pop(0)
                print("------------------------------")
                print("dispatch = PID", dispatch_pid, "now time = ", run_time)
                print("------------------------------")
                self.process[dispatch_pid].wait_end_time.append(run_time)
                self.process[dispatch_pid].burst_start_time.append(run_time)

            
            # Run End
            if len(self.ready_queue) == 0 and not self.DISPATCH and pid_count >= len(self.process):
                flag = False

            run_time += 1
        
    # Result     
    def Result(self,):
        AWT = 0
        ATT = 0
        for i in range(len(self.process)):
            for j in range(len(self.process[i].wait_start_time)):
                self.process[i].wait_time+= self.process[i].wait_end_time[j] - self.process[i].wait_start_time[j]
                AWT+=self.process[i].wait_time
                ATT+=self.process[i].turn_around_time
        print("------------RESULT------------")
        print("FCFS AWT = ",AWT/len(self.process))
        print("FCFS ATT = ",ATT/len(self.process))
        print("------------------------------")



class SJF(Scheduling):
    def __init__(self, arrival_time, burst_time, PID, priority):
        super().__init__(arrival_time, burst_time, PID, priority)
        
    def Run(self,):
        print("----------SJF START----------")
        flag = True
        run_time = 0
        pid_count = 0

        while flag:
            
            # Ready queue Enqueue
            if pid_count < len(self.process) and self.process[pid_count].arrival_time == run_time:
                #self.ready_queue.append(self.process[pid_count].PID)
                
                print("------------------------------")
                print("PID", self.process[pid_count].PID, "enqueue now time =", run_time)
                
                #shortest job check and enqueue
                if(len(self.ready_queue) == 0):
                    self.ready_queue.append(self.process[pid_count].PID)
                    self.process[pid_count].wait_start_time.append(run_time)
                
                else :
                    for i in range(len(self.ready_queue)):
                        if self.process[self.ready_queue[i]].burst_time > self.process[pid_count].burst_time:
                            self.ready_queue.insert(i, self.process[pid_count].PID)
                            self.process[pid_count].wait_start_time.append(run_time)
                            break
                
                
                print("ready_queue =", self.ready_queue)
                print("------------------------------")
                pid_count += 1

            # Dispatch
            if self.ready_queue and not self.DISPATCH:
                dispatch_start_time = run_time
                self.DISPATCH = True
                dispatch_pid = self.ready_queue.pop(0)
                print("------------------------------")
                print("dispatch = PID", dispatch_pid, "now time = ", run_time)
                print("------------------------------")
                self.process[dispatch_pid].wait_end_time.append(run_time)
                self.process[dispatch_pid].burst_start_time.append(run_time)

            # time out
            if self.DISPATCH:
                dispatch_pid = self.process[dispatch_pid].PID
                if int(self.process[dispatch_pid].burst_time - (run_time - dispatch_start_time)) == 0:
                    print("------------------------------")
                    print("time out PID", dispatch_pid, "now time = ",run_time)
                    print("------------------------------")
                    self.process[dispatch_pid].burst_end_time.append(run_time)
                    self.process[dispatch_pid].turn_around_time = run_time - self.process[dispatch_pid].arrival_time
                    self.DISPATCH = False
                    
                    
                    
            # Dispatch
            if self.ready_queue and not self.DISPATCH:
                
                dispatch_start_time = run_time
                self.DISPATCH = True
                dispatch_pid = self.ready_queue.pop(0)
                print("------------------------------")
                print("dispatch = PID", dispatch_pid, "now time = ", run_time)
                print("------------------------------")
                self.process[dispatch_pid].wait_end_time.append(run_time)
                self.process[dispatch_pid].burst_start_time.append(run_time)

            
            # Run End
            if len(self.ready_queue) == 0 and not self.DISPATCH and pid_count >= len(self.process):
                flag = False

            run_time += 1
        
    # Result     
    def Result(self,):
        AWT = 0
        ATT = 0
        for i in range(len(self.process)):
            for j in range(len(self.process[i].wait_start_time)):
                self.process[i].wait_time+= self.process[i].wait_end_time[j] - self.process[i].wait_start_time[j]
                AWT+=self.process[i].wait_time
                ATT+=self.process[i].turn_around_time
        print("------------RESULT------------")
        print("SJF AWT = ",AWT/len(self.process))
        print("SJF ATT = ",ATT/len(self.process))
        print("------------------------------")

        

class Priroty(Scheduling):
    
    def __init__(self, arrival_time, burst_time, PID, priority):
        super().__init__(arrival_time, burst_time, PID, priority)
            
    def Run(self,):
        print("----------Priority START----------")
        flag = True
        run_time = 0
        pid_count = 0

        while flag:
            
            # Ready queue Enqueue
            if pid_count < len(self.process) and self.process[pid_count].arrival_time == run_time:
                
                
                print("------------------------------")
                print("PID", self.process[pid_count].PID, "enqueue now time =", run_time)
                
                #priority check and swap queue
                if(len(self.ready_queue) == 0):
                    self.ready_queue.append(self.process[pid_count].PID)
                    self.process[pid_count].wait_start_time.append(run_time)
                
                else :
                    for i in range(len(self.ready_queue)):
                        if self.process[self.ready_queue[i]].priority > self.process[pid_count].priority:
                            self.ready_queue.insert(i, self.process[pid_count].PID)
                            self.process[pid_count].wait_start_time.append(run_time)
                            break
                
                
                print("ready_queue =", self.ready_queue)
                print("------------------------------")
                pid_count += 1

            # Dispatch
            if self.ready_queue and not self.DISPATCH:
                dispatch_start_time = run_time
                self.DISPATCH = True
                dispatch_pid = self.ready_queue.pop(0)
                print("------------------------------")
                print("dispatch = PID", dispatch_pid, "now time = ", run_time)
                print("------------------------------")
                self.process[dispatch_pid].wait_end_time.append(run_time)
                self.process[dispatch_pid].burst_start_time.append(run_time)

            # time out
            if self.DISPATCH:
                dispatch_pid = self.process[dispatch_pid].PID
                if int(self.process[dispatch_pid].burst_time - (run_time - dispatch_start_time)) == 0:
                    print("------------------------------")
                    print("time out PID", dispatch_pid, "now time = ",run_time)
                    print("------------------------------")
                    self.process[dispatch_pid].burst_end_time.append(run_time)
                    self.process[dispatch_pid].turn_around_time = run_time - self.process[dispatch_pid].arrival_time
                    self.DISPATCH = False
                    
                    
                    
            # Dispatch
            if self.ready_queue and not self.DISPATCH:
                
                dispatch_start_time = run_time
                self.DISPATCH = True
                dispatch_pid = self.ready_queue.pop(0)
                print("------------------------------")
                print("dispatch = PID", dispatch_pid, "now time = ", run_time)
                print("------------------------------")
                self.process[dispatch_pid].wait_end_time.append(run_time)
                self.process[dispatch_pid].burst_start_time.append(run_time)

            
            # Run End
            if len(self.ready_queue) == 0 and not self.DISPATCH and pid_count >= len(self.process):
                flag = False

            run_time += 1
        
    # Result     
    def Result(self,):
        AWT = 0
        ATT = 0
        for i in range(len(self.process)):
            for j in range(len(self.process[i].wait_start_time)):
                self.process[i].wait_time+= self.process[i].wait_end_time[j] - self.process[i].wait_start_time[j]
                AWT+=self.process[i].wait_time
                ATT+=self.process[i].turn_around_time
        print("------------RESULT------------")
        print("Priority AWT = ",AWT/len(self.process))
        print("Priority ATT = ",ATT/len(self.process))
        print("------------------------------")
    

        
        

def main():
    burst_time = []
    arrival_time = []
    PID = []
    priority = []
    init(arrival_time, burst_time, PID, priority)
    swap(arrival_time, burst_time, priority)
    scheduling_fcfs = FCFS(arrival_time, burst_time, PID, priority)
    scheduling_fcfs.Print()
    scheduling_fcfs.Run()
    scheduling_fcfs.Result()
    
    scheduling_sjf = SJF(arrival_time, burst_time, PID, priority)
    scheduling_sjf.Run()
    scheduling_sjf.Result()
    
    scheduling_pri = Priroty(arrival_time, burst_time, PID, priority)
    scheduling_pri.Run()
    scheduling_pri.Result()
    
    
if __name__ == "__main__":
    main()

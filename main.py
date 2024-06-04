import time
import queue
from tabulate import tabulate
import matplotlib.pyplot as plt
import pandas as pd

from scheduling import Process, Scheduling, FCFS, SJF, Priority, RoundRobin, SRT, PriorityPreemptive

def init(arrival_time, burst_time, PID, priority):
    with open("./input.txt", 'r') as f:
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




def main():
    burst_time = []
    arrival_time = []
    PID = []
    priority = []
    init(arrival_time, burst_time, PID, priority)
    swap(arrival_time, burst_time, priority)
    
    while True:
        print("-----scheduling simulation-----")
        print("1. process information")
        print("2. FCFS ")
        print("3. priority(non_preemptive)")
        print("4. SJF")
        print("5. Round Robin")
        print("6. SRT")
        print("7. priority (preemptive)")
        print("8. HRN")
        print("9. EXIT")
        
        n= input()
        if n =='1':
            sch =Scheduling(arrival_time, burst_time, PID, priority)
            sch.Print()
        elif n =='2':
            scheduling_fcfs = FCFS(arrival_time, burst_time, PID, priority)
            scheduling_fcfs.Run()
            scheduling_fcfs.Result()
        
        elif n=='3':
            scheduling_priroty = Priority(arrival_time, burst_time, PID, priority)
            scheduling_priroty.Run()
            scheduling_priroty.Result()
            
        elif n =='4':
            scheduling_sjf = SJF(arrival_time, burst_time, PID, priority)
            scheduling_sjf.Run()
            scheduling_sjf.Result()
            
        elif n == '5':
            time_quantum = 10  # 원하는 time quantum 값을 설정
            scheduling_rr = RoundRobin(arrival_time, burst_time, PID, priority, time_quantum)
            scheduling_rr.Run()
            scheduling_rr.Result()
        elif n =='6':
            time_quantum = 10  # 원하는 time quantum 값을 설정
            scheduling_srt = SRT(arrival_time, burst_time, PID, priority, time_quantum)
            scheduling_srt.Run()
            scheduling_srt.Result()
        elif n == '7':
            #priority preemptive scheduling
            scheduling_priroty_preemptive = PriorityPreemptive(arrival_time, burst_time, PID, priority)
            scheduling_priroty_preemptive.Run()
            scheduling_priroty_preemptive.Result()
        
        elif n == '8':
            #HRN
            pass
        
        elif n == '9':
            #exit
            break
        else:
            print("wrong command try again")
        
    
    
  
    
    
    
if __name__ == "__main__":
    main()

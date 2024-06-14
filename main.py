import time
import queue
from tabulate import tabulate
import matplotlib.pyplot as plt
import pandas as pd

from scheduling import Process, Scheduling, FCFS, SJF, Priority, RoundRobin, SRT, PriorityPreemptive, HRN

def init(arrival_time, burst_time, PID, priority): # init.txt와 time_quantum.txt를 읽어서 initalize func
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
            
    with open("./time_quantum.txt", 'r') as f:
        data= f.readline()
        time_quantum= int(data)
        return time_quantum

def swap(arrival_time, burst_time, priority): # PID를 Arrival time으로 설정하기 위해 만든 SWAP func
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

    
    time_quantum = init(arrival_time, burst_time, PID, priority)
    print(time_quantum)
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
        if n =='1': #FCFS Scheduling
            sch =Scheduling(arrival_time, burst_time, PID, priority)
            sch.Print()
        elif n =='2':
            scheduling_fcfs = FCFS(arrival_time, burst_time, PID, priority)
            scheduling_fcfs.Run()
            scheduling_fcfs.Result("FCFS")
            scheduling_fcfs.draw_gantt_chart()
        
        elif n=='3': #비선점 우선순위 Scheduling
            scheduling_priroty = Priority(arrival_time, burst_time, PID, priority)
            scheduling_priroty.Run()
            scheduling_priroty.Result("Priority non preemptive")
            scheduling_priroty.draw_gantt_chart()
            
        elif n =='4': #SJF SCheduling
            scheduling_sjf = SJF(arrival_time, burst_time, PID, priority)
            scheduling_sjf.Run()
            scheduling_sjf.Result("SJF")
            scheduling_sjf.draw_gantt_chart()
            
        elif n == '5': #RoundRobin 
            scheduling_rr = RoundRobin(arrival_time, burst_time, PID, priority, time_quantum)
            scheduling_rr.Run()
            scheduling_rr.Result("Round Robin")
            scheduling_rr.draw_gantt_chart()
        elif n =='6':  #SRT Scheduling
            scheduling_srt = SRT(arrival_time, burst_time, PID, priority, time_quantum)
            scheduling_srt.Run()
            scheduling_srt.Result("SRT")
            scheduling_srt.draw_gantt_chart()
        elif n == '7':
            #priority preemptive scheduling
            scheduling_priroty_preemptive = PriorityPreemptive(arrival_time, burst_time, PID, priority)
            scheduling_priroty_preemptive.Run()
            scheduling_priroty_preemptive.Result("Priority Preemptive")
            scheduling_priroty_preemptive.draw_gantt_chart()
        
        elif n == '8':
            #HRN
            scheduling_hrn = HRN(arrival_time, burst_time, PID, priority)
            scheduling_hrn.Run()
            scheduling_hrn.Result("HRN")
            scheduling_hrn.draw_gantt_chart()
        
        elif n == '9':
            #exit
            break
        else:
            print("wrong command try again")
        
    
    
  
    
    
    
if __name__ == "__main__":
    main()

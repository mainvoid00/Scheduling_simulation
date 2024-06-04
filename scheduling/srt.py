from .scheduling import Scheduling



class SRT(Scheduling):
    def __init__(self, arrival_time, burst_time, PID, priority, time_quantum):
        super().__init__(arrival_time, burst_time, PID, priority)
        self.time_quantum = time_quantum
        self.remaining_burst_time = burst_time[:]  # 남은 실행 시간을 저장
        self.finish_time = [0] * len(self.process)  # 완료 시간을 저장

    def Run(self):
        print("----------Round Robin start----------")
        flag = True
        run_time = 0
        pid_count = 0

        while flag:
            
            # Ready queue Enqueue
            if pid_count < len(self.process) and self.process[pid_count].arrival_time == run_time:
                inserted = False
                print("------------------------------")
                print("PID", self.process[pid_count].PID, "enqueue now time =", run_time)
                
                if(len(self.ready_queue) == 0):
                    self.ready_queue.append(self.process[pid_count].PID)
                    self.process[pid_count].wait_start_time.append(run_time)
                
                else :
                    for i in range(len(self.ready_queue)):
                        if self.remaining_burst_time[i] > self.remaining_burst_time[pid_count]:
                            self.ready_queue.insert(i, self.process[pid_count].PID)
                            self.process[pid_count].wait_start_time.append(run_time)
                            inserted = True
                            break

                    
                    if not inserted:
                        self.ready_queue.append(self.process[pid_count].PID)
                        self.process[pid_count].wait_start_time.append(run_time)
                        


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
                
                if int((run_time - dispatch_start_time)) == self.time_quantum or (run_time - dispatch_start_time) == self.remaining_burst_time[dispatch_pid]:
                    print("------------------------------")
                    print("time out PID", dispatch_pid, "now time = ",run_time)
                    print("------------------------------")
                    self.process[dispatch_pid].burst_end_time.append(run_time)
                    
                    self.remaining_burst_time[dispatch_pid] -=(run_time - dispatch_start_time)
                    if(self.remaining_burst_time[dispatch_pid] >0):
                        inserted= False
                        if(len(self.ready_queue) == 0):
                            self.ready_queue.append(self.process[dispatch_pid].PID)
                            self.process[dispatch_pid].wait_start_time.append(run_time)
                        
                        else :
                            for i in range(len(self.ready_queue)):
                                if self.remaining_burst_time[i] > self.remaining_burst_time[dispatch_pid]:
                                    self.ready_queue.insert(i, self.process[dispatch_pid].PID)
                                    self.process[dispatch_pid].wait_start_time.append(run_time)
                                    inserted = True
                                    break
                                
                        if not inserted:
                            self.ready_queue.append(self.process[dispatch_pid].PID)
                            self.process[dispatch_pid].wait_start_time.append(run_time)

                    else:
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
        
                    

    def Result(self):
        AWT = 0
        ATT = 0
        for i in range(len(self.process)):
            wait_time = 0
            for j in range(len(self.process[i].wait_start_time)):
                
                if j < len(self.process[i].wait_end_time):
                    self.process[i].wait_time += (self.process[i].wait_end_time[j] - self.process[i].wait_start_time[j])

            AWT += self.process[i].wait_time
            ATT += self.process[i].turn_around_time
        print("------------RESULT------------")
        print("SRT AWT = ", AWT / len(self.process))
        print("SRT ATT = ", ATT / len(self.process))
        print("------------------------------")
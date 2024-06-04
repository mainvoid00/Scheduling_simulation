from .scheduling import Scheduling


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
                inserted = False
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

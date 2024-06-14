from .scheduling import Scheduling


class HRN(Scheduling):
    def __init__(self, arrival_time, burst_time, PID, priority):
        super().__init__(arrival_time, burst_time, PID, priority)
    


    def Run(self,):
        print("----------Priority Preemptive START----------")
        flag = True
        run_time = 0
        pid_count = 0
        hrn_priority =[len(self.process)]
        while flag:

            if pid_count < len(self.process) and self.process[pid_count].arrival_time == run_time:
                self.ready_queue.append(self.process[pid_count].PID)
                self.process[pid_count].wait_start_time.append(run_time)
                print("------------------------------")
                print("PID", self.process[pid_count].PID, "enqueue now time =", run_time)
                print("ready_queue =", self.ready_queue)
                print("------------------------------")
                pid_count += 1

            if self.ready_queue and not self.DISPATCH:
                
                for i in range(len(self.ready_queue)):
                    max_hrn_index=-1
                    max_hrn= -1
                    print("pid",self.ready_queue[i],"hrn =", ((run_time-self.process[self.ready_queue[i]].wait_start_time[0]) + self.process[self.ready_queue[i]].burst_time)/self.process[self.ready_queue[i]].burst_time)
                    if max_hrn < ((run_time-self.process[self.ready_queue[i]].wait_start_time[0]) + self.process[self.ready_queue[i]].burst_time)/self.process[self.ready_queue[i]].burst_time :
                        max_hrn = ((run_time-self.process[self.ready_queue[i]].wait_start_time[0]) + self.process[self.ready_queue[i]].burst_time)/self.process[self.ready_queue[i]].burst_time
                        max_hrn_index = i
                    
                dispatch_start_time = run_time
                self.DISPATCH = True
                dispatch_pid = self.ready_queue.pop(max_hrn_index)
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
                    print("time out PID", dispatch_pid, "now time = ", run_time)
                    print("------------------------------")
                    self.process[dispatch_pid].burst_end_time.append(run_time)
                    self.process[dispatch_pid].turn_around_time = run_time - self.process[dispatch_pid].arrival_time
                    self.DISPATCH = False

            #dispatch
            if self.ready_queue and not self.DISPATCH:
                
                for i in range(len(self.ready_queue)):
                    max_hrn_index=-1
                    max_hrn= -1
                    print("pid",self.ready_queue[i],"hrn =", ((run_time-self.process[self.ready_queue[i]].wait_start_time[0]) + self.process[self.ready_queue[i]].burst_time)/self.process[self.ready_queue[i]].burst_time)
                    if max_hrn < ((run_time-self.process[self.ready_queue[i]].wait_start_time[0]) + self.process[self.ready_queue[i]].burst_time)/self.process[self.ready_queue[i]].burst_time :
                        max_hrn = ((run_time-self.process[self.ready_queue[i]].wait_start_time[0]) + self.process[self.ready_queue[i]].burst_time)/self.process[self.ready_queue[i]].burst_time
                        max_hrn_index = i
                    
                dispatch_start_time = run_time
                self.DISPATCH = True
                dispatch_pid = self.ready_queue.pop(max_hrn_index)
                print("------------------------------")
                print("dispatch = PID", dispatch_pid, "now time = ", run_time)
                print("------------------------------")
                self.process[dispatch_pid].wait_end_time.append(run_time)
                self.process[dispatch_pid].burst_start_time.append(run_time)
            

            # Run End
            if len(self.ready_queue) == 0 and not self.DISPATCH and pid_count >= len(self.process):
                flag = False

            run_time += 1


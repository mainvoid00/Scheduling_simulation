from .process import Process
from tabulate import tabulate
class Scheduling:
    def __init__(self, arrival_time, burst_time, PID, priority):
        self.ready_queue = []
        self.process = []
        self.DISPATCH = False
        self.PID = PID
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



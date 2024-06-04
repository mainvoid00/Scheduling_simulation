from .process import Process
from tabulate import tabulate
import matplotlib.pyplot as plt
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

    
    def Result(self, sch_name):
        AWT = 0
        ATT = 0
        for i in range(len(self.process)):
            for j in range(len(self.process[i].wait_start_time)):
                self.process[i].wait_time += self.process[i].wait_end_time[j] - self.process[i].wait_start_time[j]
            AWT += self.process[i].wait_time
            ATT += self.process[i].turn_around_time
        print("------------RESULT------------")
        print(f"{sch_name} AWT =", AWT / len(self.process))
        print(f"{sch_name} ATT = ", ATT / len(self.process))
        print("------------------------------")

    def draw_gantt_chart(self):
        fig, gnt = plt.subplots()

        gnt.set_xlabel('Time')
        gnt.set_ylabel('Processes')

        y_ticks = [i for i in range(len(self.process))]
        y_labels = [f'P{process.PID}' for process in self.process]
        gnt.set_yticks(y_ticks)
        gnt.set_yticklabels(y_labels)

        gnt.grid(True)


        max_time = 0  # 최대 시간을 저장할 변수

        for i, process in enumerate(self.process):
            for j in range(len(process.wait_start_time)):
                gnt.broken_barh([(process.wait_start_time[j], process.wait_end_time[j] - process.wait_start_time[j])], 
                                (i - 0.4, 0.8), facecolors=('tab:gray'))
                max_time = max(max_time, process.wait_end_time[j])  # 최대 시간을 업데이트
            for j in range(len(process.burst_start_time)):
                gnt.broken_barh([(process.burst_start_time[j], process.burst_end_time[j] - process.burst_start_time[j])], 
                                (i - 0.4, 0.8), facecolors=('tab:blue'))
                max_time = max(max_time, process.burst_end_time[j])  # 최대 시간을 업데이트

        gnt.set_xticks(range(0, max_time + 1))  # x축 눈금을 1단위로 설정


        plt.show()



class Process:
    def __init__(self, burst_time, priority, arrival_time, PID):
        self.burst_time = burst_time # Process의 burst time
        self.priority = priority     # Process의 우선순위
        self.arrival_time = arrival_time # Process의 도착시간
        self.PID = PID                  # Process의 PID
        self.wait_start_time = []       # Scheduling이 동작할 때 wait을 시작하는 시간의 list
        self.wait_end_time = []         # Scheduling이 동작할 때 wait이 끝나는 시간의 list
        self.burst_start_time = []      # process가 distpatch를 시작할 때 시작하는 list
        self.burst_end_time = []        # process가 timeout을 할 때의 list
        self.wait_time = 0              # process의 wait_time
        self.turn_around_time = 0       # process의 turn_around time
        self.remaining_burst_time = self.burst_time # service time 남은 시간

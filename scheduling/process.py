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
        self.wait_time = 0
        self.turn_around_time = 0
        self.remaining_burst_time = self.burst_time

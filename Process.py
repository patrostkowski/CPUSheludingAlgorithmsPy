class Process():
    done = False
    running = False
    waiting = 0
    turnaround = 0   

    def __init__(self, name, arrival, burst, priority):
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.priority = priority


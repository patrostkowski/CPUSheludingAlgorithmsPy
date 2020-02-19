from Algorithm import Algorithm
import copy

class FCFS(Algorithm):
    def Calculate(self, processes):
        process = []
        process = copy.deepcopy(processes)
        process = sorted(process, key=lambda x: x.arrival)

        self.clock_time = [0 for i in range(len(process))]

        process[0].waiting, process[0].turnaround, process[0].done = 0, process[0].burst, True

        for i in range(1,len(process)):
            self.clock_time[i] = self.clock_time[i-1] + process[i-1].burst
            process[i].waiting = self.clock_time[i] - process[i].arrival

            if process[i].waiting < 0: process[i].waiting = 0

            process[i].turnaround = process[i].waiting + process[i].burst
            process[i].done = True 

        self.FindSum(process)
        
        return process
from Algorithm import Algorithm
from Process import Process
import copy
import os
import sys

class RR(Algorithm):
    def Calculate(self, processes):
        n = 0
        id = 0
        queue = []
        done = []
        qt = 2
        clock_time = 0

        process = copy.deepcopy(processes)
        process = sorted(process, key=lambda x: x.arrival)
       
        while n != len(process):
            for i in range(0, len(process)):
                if process[i].done != True:
                    if process[i].arrival == 0 and process[i].running == False:
                        process[i].running = True
                        temp1 = copy.deepcopy(process[i])
                        queue.append(temp1)
                    elif process[i].arrival <= clock_time and process[i].running == False:
                        process[i].running = True
                        temp1 = copy.deepcopy(process[i])
                        queue.append(temp1)

            if id == len(queue):
                id = 0

            if len(queue) > 0:
                if queue[int(id)].burst > qt:
                    queue[int(id)].burst -= qt
                    id += 1
                    clock_time += qt                    
                elif queue[int(id)].burst <= qt:
                    process[id].done = True
                    clock_time += queue[id].burst
                    queue[id].running = False
                    for i in range(0, len(process)):
                        if queue[id].name == process[i].name and queue[id].arrival == process[i].arrival:
                            process[i].turnaround = clock_time - process[i].arrival
                            process[i].waiting = process[i].turnaround - process[i].burst
                            temp2 = copy.deepcopy(process[i])
                            done.append(temp2)
                            queue.remove(queue[id])                            
                            n += 1
                            break                  

        self.FindSum(done)
                 
        return done
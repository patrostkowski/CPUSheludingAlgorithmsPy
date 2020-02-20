from Algorithm import Algorithm
from Process import Process
import copy
import os
import sys

class PBS(Algorithm):
    def Calculate(self, processes):
        n = 0
        id = 0
        queue = []
        done = []
        clock_time = 0
        highest_list = []

        process = copy.deepcopy(processes)
        process = sorted(process, key=lambda x: x.arrival)

        for i in range(len(process)):
            if process[i].arrival == 0:
                highest_list.append(process[i].priority)

        highest_val = max(highest_list)

        while n != len(process):  
            for i in range(len(process)):
                if process[i].running == False:
                    if process[i].arrival ==0 and process[i].priority == highest_val:
                        done.append(process[i])
                        done[0].waiting = 0
                        done[0].turnaround = done[0].burst
                        process[i].running = True
                        clock_time = done[0].burst
                        n += 1
                    elif process[i].arrival <= clock_time:
                        queue.append(process[i])
                        process[i].running = True

            if len(queue) > 0:
               highest_val = max(q.priority for q in queue)

            if id == len(queue):
                id = 0

            if queue[id].arrival <= clock_time and queue[id].priority == highest_val:
                queue[id].waiting = clock_time - queue[id].arrival
                queue[id].turnaround = queue[id].waiting + queue[id].burst
                for q in queue:
                    q.priority += 1
                done.append(queue[id])
                clock_time += queue[id].burst
                queue.remove(queue[id])
                id = 0
                n += 1
            else:
                id += 1

        self.FindSum(done)

        return done
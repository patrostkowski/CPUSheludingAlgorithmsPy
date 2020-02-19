from Algorithm import Algorithm
import copy
import os
import sys

class SJF(Algorithm):
    def Calculate(self, processes):
        n = 0
        id = 0
        lowest_list = []
        queue = []
        done = []

        process = copy.deepcopy(processes)
        process = sorted(process, key=lambda x: x.arrival)

        for i in range(0, len(process)):
            if process[i].arrival == 0:
                lowest_list.append(process[i].burst)

        lowest_val = min(lowest_list)

        while n != len(process):
            for i in range(0, len(process)):
                if process[i].running == False:
                    if process[i].arrival == 0 and process[i].burst == lowest_val:
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
               lowest_val = min(q.burst for q in queue)

            if id == len(queue):
                id = 0

            if queue[id].arrival <= clock_time and queue[id].burst == lowest_val:
                queue[id].waiting = clock_time - queue[id].arrival
                queue[id].turnaround = queue[id].waiting + queue[id].burst
                done.append(queue[id])
                clock_time += queue[id].burst
                queue.remove(queue[id])
                id = 0
                n += 1
            else: 
                id += 1

        self.FindSum(done)

        return done
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

            os.system('cls')
            print("                     PROCESS")
            self.help(process,queue,done, clock_time, id, n)

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

            os.system('cls')
            print("                     QUEUE")
            self.help(process,queue,done, clock_time, id, n)

            if len(queue) > 0:
                if queue[id].burst > qt:
                    queue[id].burst -= qt
                    print(f'Decreased {queue[id].name}')
                    id += 1
                    clock_time += qt
                elif queue[id].burst <= qt:
                    for p in process:
                        if  p.name == queue[id].name and p.arrival == queue[id].arrival:
                            temp2 = copy.deepcopy(p)
                            done.append(temp2)
                            del queue[id]
                            clock_time += qt
                            id = 0
                            n += 1


            '''                     
            if len(queue) > 0:
                if queue[id].burst <= qt:
                    process[id].done = True
                    print(f'Finished {queue[id].name}')
                    clock_time += queue[id].burst
                    queue[id].running = False
                    for i in range(0, len(process)):
                        if queue[id].name == process[i].name and queue[id].arrival == process[i].arrival:
                            temp2 = copy.deepcopy(process[i])
                            done.append(temp2)
                            queue.remove(queue[id])                              
                    n += 1                     
            elif queue[id].burst >= qt:
                queue[id].burst -= qt
                print(f'Decreased {queue[id].name}')
                id += 1
                clock_time += qt
            '''

            if id == len(queue):
                id = 0
                 
        return done

    def help(self, process, queue, done, clock, i, m):
        #os.system('cls')
        if len(queue) > 0: print(queue[i].name)
        print(f'clock: {clock}')
        print(f'id: {i}')
        print(f'n: {m}')
        print(f'len proc: {len(process)}')
        print(f'len que: {len(queue)}')
        print(f'len done: {len(done)}')
        print('                             PROCESS')
        self.Results(process)
        print('                             QUEUE')
        self.Results(queue)
        print('                             DONE')
        self.Results(done)
        input('click key')

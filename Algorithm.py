import os
import sys
from datetime import datetime
from contextlib import redirect_stdout
import copy

class Algorithm():
    avarage_wait_time = 0
    avarage_turnaround_time = 0
    clock_time = 0

    def __init__(self, name):
        self.name = name

    def FindSum(self, process):
        self.avarage_turnaround_time = (sum(p.turnaround for p in process) / len(process))
        self.avarage_wait_time = (sum(p.waiting for p in process) / len(process))

    def Results(self, process):
        print(f'Algorithm Name - {self.name}')
        print('Name         Arrival    Burst      Priority  Turnaround  Waiting')
        for i in range(0, len(process)):
            print(f'{process[i].name}     {process[i].arrival}          {process[i].burst}          {process[i].priority}         {process[i].turnaround}           {process[i].waiting}')
        print(f'Avarage Waiting Time - {self.avarage_wait_time}')
        print(f'Avarage Turnaround Time - {self.avarage_turnaround_time}')
        return process

    def SaveToFile(self, process):
        with open(f'/Users/Patryk/Desktop/{self.name}{str(datetime.now().strftime("%d-%m-%Y %H-%M-%S"))}.txt', 'w') as f:
            with redirect_stdout(f):
                self.Results(process)

                '''
    def help(self, process, queue, done, clock, i, m, low):
        os.system('cls')
        print(f'clock: {clock}')
        print(f'id: {i}')
        print(f'n: {m}')
        print(f'lowest val: {low}')
        print(f'len que: {len(queue)}')
        print('                             PROCESS')
        self.Results(process)
        print('                             QUEUE')
        self.Results(queue)
        print('                             DONE')
        self.Results(done)
        input('click key')
'''
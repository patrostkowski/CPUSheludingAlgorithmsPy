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

    def SaveToFile(self, path, date, process):
        with open(f'{path}/{self.name}{date}.txt', 'w') as f:
            with redirect_stdout(f):
                self.Results(process)
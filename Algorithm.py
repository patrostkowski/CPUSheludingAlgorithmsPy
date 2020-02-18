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

    def Results(self, process):
        print(f'Algorithm Name - {self.name}')
        print('Name         Arrival    Burst      Priority  Turnaround  Waiting')
        for i in range(0, len(process)):
            print(f'{process[i].name}     {process[i].arrival}          {process[i].burst}          {process[i].priority}         {process[i].turnaround}           {process[i].waiting}')
        print(f'Avarage Waiting Time - {self.avarage_wait_time}')
        print(f'Avarage Turnaround Time - {self.avarage_turnaround_time}')

    def SaveToFile(self, process):
        with open(f'/Users/Patryk/Desktop/{self.name}{str(datetime.now().strftime("%d-%m-%Y %H-%M-%S"))}.txt', 'w') as f:
            with redirect_stdout(f):
                self.Results(process)
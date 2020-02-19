import os
import sys
from Process import Process
from Algorithm import Algorithm
from FCFS import FCFS
from SJF import SJF
from RR import RR
from datetime import datetime

def printf(process):
    print('Name         Arrival    Burst      Priority')
    for i in range(0, len(process)):
        print(f'{process[i].name}     {process[i].arrival}          {process[i].burst}          {process[i].priority}')

os.system('cls')

if len(sys.argv)-1 == 0: 
    print('No arguments passed. Srcipt will be shut down.')
    sys.exit()

try:
    with open(f'/Users/Patryk/Desktop/{sys.argv[1]}', 'r') as f:
        f_content = f.readlines()
        processes = [line.strip().split(' ') for line in f_content] 
except FileNotFoundError:
    print('Cant load a file.')
    sys.exit()
else:
    print('File loaded.')

process = [Process(processes[i][0], 
int(processes[i][1]),
int(processes[i][2]), 
int(processes[i][3])) for i in range(0, len(processes))] # Creates list of objects (Processes) 

'''
a = Algorithm('a')
a.SaveToFile(process)
a.Results(process)
'''

fcfs = FCFS('fcfs')
sjf = SJF('sjf')
rr = RR('rr')

#fcfs.SaveToFile(fcfs.Results(fcfs.Calculate(process)))
#sjf.SaveToFile(sjf.Results(sjf.Calculate(process)))

#fcfs.Results(fcfs.Calculate(process))
#sjf.Results(sjf.Calculate(process))
rr.Results(rr.Calculate(process))



import os
import sys
from Process import Process
from Algorithm import Algorithm
from FCFS import FCFS
from SJF import SJF
from RR import RR
from PBS import PBS
from datetime import datetime

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

date_now = str(datetime.now().strftime("%d-%m-%Y %H-%M-%S"))
path = f'/Users/Patryk/Desktop/Algorithms{date_now}'

fcfs = FCFS('fcfs')
sjf = SJF('sjf')
rr = RR('rr')
pbs = PBS('pbs') 

os.mkdir(path)

fcfs.SaveToFile(path, date_now, fcfs.Results(fcfs.Calculate(process)))
sjf.SaveToFile(path, date_now, sjf.Results(sjf.Calculate(process)))
rr.SaveToFile(path, date_now, rr.Results(rr.Calculate(process)))
pbs.SaveToFile(path, date_now, pbs.Results(pbs.Calculate(process)))
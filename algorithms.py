import os
import sys
import time
from Process import Process

def printf(process):
    #os.system('cls')
    print('name         arrival    burst      priority')
    for i in range(0, len(process)):
        print(f'{process[i].name}     {process[i].arrival}          {process[i].burst}          {process[i].priority}')

if len(sys.argv)-1 == 0: 
    print('No arguments passed. Srcipt will be shut down.')
    time.sleep(1)
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

sortProcess = sorted(process, key=lambda x: x.arrival)
printf(sortProcess)

import random
import time
np= int(input("Enter no of processes: "))
processes=[]
for i in range(np):
    processes.append(i)

print(processes)

def switch(p,c):
    if(c==1):
        print("Process ",p," is in the critical section.")
        time.sleep(2)
        print("Process ",p, " exits CS")
        i=processes.index(p)
        print("Process ",p," passes the token to Process ",processes[(i+1)%np])
    else:
        i=processes.index(p)
        print("Process ",p,"  passes the token to Process ",processes[(i+1)%np])
i=0
while True:    
    print("Process ",processes[(i)%np]," has the token")
    choice=int(input("Enter \n1. Enter CS\n2. Pass the token\n"))
    switch(processes[i],choice)
    i=(i+1)%np

import random
msg=0
def ring(i,j):
    global msg
    #print(processes[i])
    #print(processes[j])
    print("Process", processes[i] , " sends a messages to " , processes[j])
    msg=msg+1
    l.append(processes[i])
    return l

choice=0
while(choice!=2):
    choice=int(input("Enter 1 for election. or 2 to quit"))
    if(choice == 1):
        nop=int(input("Enter number of processes: "))
        processes=[]
        for i in range(nop):
            processes.append(i+1)
        print(processes)
        print(processes[nop-1])
        l=[]
        print("Coordinator " ,processes[nop-1] ," is not responding" )
        processes.remove(processes[nop-1])
        p=random.randint(0,nop-2)
        print(p)
        print(processes)
        print("Process ",processes[p] , " notices that the coordinator is not responding")
        for k in range(p,nop-1):
            #print((k)%(nop-1),(k+1)%(nop-1))
            a=ring((k)%(nop-1),(k+1)%(nop-1))
            
        for k in range(0,p):
            a=ring(k,k+1)

        for j in processes[:processes.index(max(a))]:
            if(j!=processes[p]):
                print("Process ",processes[p] , " informs ",j," that " ,max(a), " is the coordinator, ")
                msg=msg+1
        print("No of messages passed : ",msg)

    

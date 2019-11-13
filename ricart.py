import random
import threading
import time

np=int(input("Enter no of processes: "))
processes=[]
for i in range(np):
	processes.append(i)

timestamp=random.sample(range(0,np+3),np)
print("Processes",processes)
print("TimeStamp of the processes : ",timestamp)
cs=[]
queue=[]
msg=0
def removecs(w):
	cs.remove(w)
	
def ricart(pid,time):
        global msg
        count=0
        for i in processes:
                if(i not in requestingp and i not in cs):
                        print("Process ",i," sends OK to process ",pid) 
                        count=count+1
                        msg=msg+1
                else:
                        if(timestamp[processes.index(pid)] < timestamp[processes.index(i)]):
                                print("Process ",i," sends OK to process ", pid)
                                count=count+1
                                msg=msg+1
                        else:
                                if(pid not in queue):
                                        queue.append(pid)
        return count			
r=random.randint(0,int(np/2))
requestingp=random.sample(processes,r)
print("Requesting Processes : ",requestingp)
o=[]
now=time.time()
while(len(queue) !=0 or len(requestingp) !=0):
        o=[]
        if(len(cs)!=0):
                time.sleep(1)
                removecs(w)
        else:
                if(len(queue) <=0):
                        for i in requestingp:
                                o.append(ricart(i,timestamp[processes.index(i)]))
                else:
                        for i in queue:
                                o.append(ricart(i,timestamp[processes.index(i)]))
                w=requestingp[o.index(max(o))]	
                print("\n\nPROCESS ",w ," WINS\n")
                print("no of messages : ",msg)
                cs.append(w)
                queue.remove(w)
                requestingp.remove(w)
                

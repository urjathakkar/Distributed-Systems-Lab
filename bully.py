import random
	
np= int(input("Enter no of processes: "))
processes=[]
for i in range(np):
        processes.append(i)
msg=0

def bully(p,n):
        #print("process",n)
        global msg
        rp=[]
        print("Process ",n," holds the election" )
        #print("called by",p)
        y=p.index(n)
        #print(y+1)
        #print(p)
        rp=p[y:]
        #print("before",rp)
        for i in rp:
                if(i!=n):
                        if(i==t):
                                print("Process ", n, " notices process ", i, " is down")
                                msg=msg+1
                        else:
                                print("Process",n, " sends election message to Process ",i)
                                msg=msg+1               
        if(len(rp)== 2):
                for i in processes[:processes.index(rp[0])]:
                        print("Process ", rp[0], " informs " ,i, " that it is the coordinator")
                        msg=msg+1
                print("Process" ,rp[0] , " is the coordinator")
        else:
                #print("b",rp)
                rp.remove(rp[0])
                #print("after",rp)
                for i in rp:
                        if(i!=t):
                                print(i, " sends OK to ",n )
                                msg=msg+1
                bully(rp,rp[0])
        return msg

while(1):
        print(processes)
        t=max(processes)
        #print(max(processes) , "has crashed")
        #t=random.randint(0,(np-1))
        print("Process", t , " has crashed ")	
        p=int(input("Enter the requesting process: "))
        if(p!=t):
                m=bully(processes,p)
                print("No of messages passed :",m)
        


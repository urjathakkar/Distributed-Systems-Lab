queue=[]
cs=0
def req(p):
        global cs
        global queue
        #print(queue)        					
        if(cs==0):
                if(p not in queue):
                        queue.append(p)
                else:
                        queue=queue
                cs=1
                print(p, " is in critical section.")
                #print(queue)
        elif(cs==1):
                if(p not in queue):
                        queue.append(p)
                else:
                        queue=queue
                
                #queue.append(p)
                print(queue)
def rel():
        global cs
        global queue
        print("release")
        print(queue)
        if(cs==1):
                cs=0
                print(queue[0] ,"removed from critical section")		
                queue=queue[1:]
                print(queue)
        if(len(queue)>0): 
                req(queue[0])
while(1):

        a=int(input("Enter \n 0 request \n 1 for release \n"))
        if(a==0):
                p=int(input("Enter process number: "))
                req(p)
        elif(a==1):
                rel()
        else:
                sys.exit(0)		
        #switch(a)

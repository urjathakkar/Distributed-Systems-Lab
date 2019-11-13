import threading
import socket
import pickle			 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
port = 12345				
s.bind(('', port))		 
s.listen(5)	 

def sortlist(data):
    return data.sort()

def word(s):
    d = {}
    s = s.split()
    words, count = [], []
    temp = sorted(s,key=s.count,reverse=True)
    for x in temp:
        if  x not in words:
            words.append(x)
    print(words)

    count = [s.count(x) for x in words]
    print(count)

    d['WORDS'] = words
    d['COUNT'] = count
    print(d)
    return d


while True: 
    c, addr = s.accept()	 
    print('Got connection from', addr) 
    data = c.recv(4096)
    if type(data) == list:
        data = pickle.loads(data)
        t1 = threading.Thread(target=sortlist, args=(data,)) 
        t1.start()
        t1.join()
    else:
        data = pickle.loads(data)
        t2 = threading.Thread(target=word, args=(data,)) 
        t2.start()
        t2.join()

    data = pickle.dumps(data)
    c.send(data)
    c.close() 

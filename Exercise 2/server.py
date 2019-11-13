import socket
import pickle
from math import factorial as fact
import multiprocessing as mp
import os
import time

f = []
def factlist(l):
    for i in l:
        f.append(fact(i))
    return f
HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)



while True:
    c, addr = s.accept()
    print('Connected by', addr)
    data = c.recv(4096)
    data=pickle.loads(data)
    p = mp.Pool()
    start = time.time()
    result = p.map(factlist,data)
    duration = time.time() - start
    print("Program ran for " + duration + " seconds")
    data=pickle.dumps(result)
    c.send(data)
    c.close() 

from random import randint as rand
import pickle
import socket			 



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 

port = 12348				
s.connect(('127.0.0.1', port)) 

n = rand(1,7)
l = []
for i in range(n):
    l.append(rand(1,20))
print(l)

l = pickle.dumps(l)
s.send(l)

data = s.recv(4096)
data = pickle.loads(data)

s.close()	 

print(data)

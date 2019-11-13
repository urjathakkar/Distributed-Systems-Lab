import numpy as np
import pickle
import socket			 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 

port = 12345				
s.connect(('127.0.0.1', port)) 


l = np.random.normal(0, 0.1, 50)
l = pickle.dumps(l)
s.send(l)

data = s.recv(4096)
data = pickle.loads(data)

s.close()	 

print(data)

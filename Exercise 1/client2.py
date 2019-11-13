import pickle
import socket			 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 

port = 12345				
s.connect(('127.0.0.1', port)) 

l = "John is a nice guy and he is a player"
l = pickle.dumps(l)
s.send(l)

data = s.recv(4096)
data = pickle.loads(data)

s.close()	 

print(data)

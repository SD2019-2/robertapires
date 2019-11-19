
#!/usr/bin/python

import socket
import sys

s = socket.socket()
#host = socket.gethostname()
host = '172.16.16.24'
port = 12345
s.bind((host, port))

s.listen(1)

c, addr = s.accept()

nome = c.recv(1024)
cargo = c.recv(1024)
salario = float((c.recv(1024)))

if cargo == 'operador':
	salario += salario * 0.20
if cargo == 'programador':
	salario += salario * 0.18
	
salario_convert = str(salario)

c.send(salario_convert)

c.close()
sys.exit()

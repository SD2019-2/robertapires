#!/usr/bin/python

import socket
import sys

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))

nome = raw_input ("Nome: ")
s.send(nome)
cargo = raw_input ("Cargo: ")
s.send(cargo)
salario = raw_input ("Salario: ")
s.send(salario)

novo_salario = s.recv(1024)

print (nome + " passara a receber " + novo_salario)

s.close()
sys.exit()

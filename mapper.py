#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.split()
    nome, mes, puntos = data
    print(nome+" "+puntos)
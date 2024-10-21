#!/usr/bin/python
import sys

pointsTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.split()
    
    thisKey, thisValue = data_mapped

    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if oldKey and (oldKey != thisKey):
        print(oldKey+" "+str(pointsTotal))
        oldKey = thisKey
        pointsTotal = 0

    oldKey = thisKey
    pointsTotal += int(thisValue)

# Escribe o ultimo par, unha vez rematado o bucle
if oldKey != None:
    print(oldKey+" "+str(pointsTotal))
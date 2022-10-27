import sys
import os
import random

matrix = []
subtour = []
clients_on_hold = ['1','2','3','4','5']
tsp = False
trip = clients_on_hold[:]

with open('insercion_barata_dataset.txt') as file:
    for line in file:
        matrix.append(line.split())
#while(tsp == False):

start_index = random.randint(0, len(trip)-1)
print(start_index)
start_client = int(trip[start_index])
print(start_client)

clients_on_hold.remove(str(start_client))
current_node = matrix[start_client]
print(current_node)
save = current_node[:]#Slide operator para guardar el arreglo inicial
calc = current_node[:]
calc.pop(0) #Eliminar el elemento en base al indice, en este caso se eliminó El cliente para tener puros numeros
print(calc)
calc.remove('0')#Eliminar el 0 para evitar fallos de logica
print(calc)

for i in range(0,len(calc)):
    calc[i] = int(calc[i])

cheapest = min(calc)#Se obtiene el numero del cliente del precio mas bajo para seguir con el proximo cliente
#print(next_client)
next_client = save.index(str(cheapest))
clients_on_hold.remove(str(next_client))
subtour = [start_client, next_client, start_client]
new_subtour = subtour[:]
print(subtour)
print(clients_on_hold)
#print(save)
#print(clients_on_hold[0])
costs = []
clients = []
less_price = 9999
while(len(clients_on_hold) != 0):
    
    k = int(clients_on_hold[0])
    Cik = matrix[start_client][k]
    Ckj = matrix[k][next_client]
    Cij = matrix[start_client][next_client]
    #clients.append(k)
    costx = int(Cik)+int(Ckj)-int(Cij)
    if(costx <= less_price):
        less_price = costx
        before = True
        client_selected = k
    costs.append(costx)
    
    Cik = matrix[next_client][k]
    Ckj = matrix[k][start_client]
    Cij = matrix[next_client][start_client]
    costx = int(Cik)+int(Ckj)-int(Cij)
    if(costx <= less_price):
        less_price = costx
        before = False
        client_selected = k
    #clients.append(k)
    costs.append(costx)
    
    #prit(k)
    #print('-')
    #print(Cik)
    #print(Ckj)
    #print(Cij)
    
    clients_on_hold.pop(0)

print(costs)

result = ["Validaciones: ",less_price,before,client_selected]
print(result)
new_subtour.append(min(costs))
#print(new_subtour)
#print(*matrix, sep="\n")

#for client in matrix:



#print(start)
#print(*matrix, sep="\n")

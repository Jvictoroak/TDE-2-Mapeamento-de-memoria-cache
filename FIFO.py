sequencia_1 = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
sequencia_2 = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
sequencia_3 = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]

quadros = 8

def fifo(sequencia, quadros):
    memoria = []
    for i in range(len(sequencia)):
        if sequencia[i] in memoria:
            continue
        if(len(memoria) >= quadros):
            memoria.pop(0)
        memoria.append(sequencia[i])
    return memoria

print(fifo(sequencia_1, quadros))
print(fifo(sequencia_2, quadros))
print(fifo(sequencia_3, quadros))
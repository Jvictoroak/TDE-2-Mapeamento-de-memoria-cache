# remove a utilizada mais recentemente
sequencia = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
quadros = 8
ativo = []

for i in range(len(sequencia)):
    print(ativo, sequencia[i])
    if sequencia[i] in ativo:
        ativo.remove(sequencia[i])
        ativo.append(sequencia[i])
        continue
    if(len(ativo) >= 8):
        ativo.pop(-1)   
    ativo.append(sequencia[i])

print(ativo)
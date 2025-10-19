sequencia_1 = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]  # primeira sequência de referências
sequencia_2 = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]  # segunda sequência de referências
sequencia_3 = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]  # terceira sequência de referências

quadros = 8  # número de quadros disponíveis na cache

def mru(sequencia, quadros):
    memoria = []  # lista que representa os quadros atuais
    for i in range(len(sequencia)):  # percorre cada referência na sequência
        if sequencia[i] in memoria:  # se a página já está em cache
            memoria.remove(sequencia[i])  # remove a página da posição antiga
            memoria.append(sequencia[i])  # coloca a página no final
            continue  # passa para a próxima referência
        if(len(memoria) >= quadros):  # se todos os quadros estão ocupados
            memoria.pop(-1)   # remove o mais recentemente usado
        memoria.append(sequencia[i])  # adiciona a nova página
    return memoria  # retorna o estado final dos quadros

print(mru(sequencia_1, quadros))  # imprime o resultado para a sequência 1
print(mru(sequencia_2, quadros))  # imprime o resultado para a sequência 2
print(mru(sequencia_3, quadros))  # imprime o resultado para a sequência 3
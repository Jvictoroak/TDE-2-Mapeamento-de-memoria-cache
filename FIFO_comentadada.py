sequencia_1 = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]  # primeira sequência de referências
sequencia_2 = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]  # segunda sequência de referências
sequencia_3 = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]  # terceira sequência de referências

quadros = 8  # número de quadros disponíveis na cache

def fifo(sequencia, quadros):
    ativo = []  # lista que representa os quadros atuais
    for i in range(len(sequencia)):  # percorre cada referência na sequência
        if sequencia[i] in ativo:  # se a página já está em cache
            continue  # passa para a próxima iteração
        if(len(ativo) >= quadros):  # se todos os quadros estão ocupados
            ativo.pop(0)  # remove o primeiro elemento
        ativo.append(sequencia[i])  # adiciona a nova página no final
    return ativo  # retorna o estado final dos quadros

print(fifo(sequencia_1, quadros))  # imprime o resultado para a sequência 1
print(fifo(sequencia_2, quadros))  # imprime o resultado para a sequência 2
print(fifo(sequencia_3, quadros))  # imprime o resultado para a sequência 3
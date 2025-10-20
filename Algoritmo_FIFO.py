Paginas_A = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
Paginas_B = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
Paginas_C = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]

def FIFO (Conjunto_paginas):
    Paginas_ativas = []
    contador = 0
    for i in Conjunto_paginas:
        if i not in Paginas_ativas:
            if len(Paginas_ativas) >= 8:
                Paginas_ativas[contador] = i
                contador = contador + 1
            else: Paginas_ativas.append(i)
            if contador > 7:
                contador = 0
         
    return Paginas_ativas

print("A:", FIFO(Paginas_A))
print("B:", FIFO(Paginas_B))
print("C:", FIFO(Paginas_C))

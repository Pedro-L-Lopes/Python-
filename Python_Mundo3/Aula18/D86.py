matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()












#criar matriz de dimensao 3x3 0
#                             1
#                             2  
#                               0 1 2
#preencha com os valores lidos pelo teclado 
#No final mostre a matriz na tela com a formatação correta 
import lista_1

teste = lista_1.Lista1_EDA()
multiplica = teste.multiplica(4, 5)
print(multiplica)

divide = teste.divide(625, 5)
print(divide)

potencia =  teste.potencia(10, 3)
print(potencia)

primo = teste.primo(9)
print(primo)

fatorial = teste.fatorial(2)
print(fatorial)

inteiros = teste.inteiros(5)
print(inteiros)

fibonacci = teste.fibonacci(14)
print(*fibonacci)

multiplos = teste.multiplos(10)
print(*multiplos)

list = [10, 1, 2, 4, 7, 3]

maior = teste.maior(list)
print(maior)

min = teste.menor(list)
print(min)

mean = teste.media(list)
print(mean)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma_matriz = teste.somatriz(matriz)
print(soma_matriz)

soma_coluna = teste.somacoluna(matriz)
print(soma_coluna)

soma_diagonal = teste.somadiagonal(matriz)
print(soma_diagonal)


list_2 = [5, 6, 7, 10, 9, 3]
pertence = teste.pertence(list, list_2)
print(pertence)
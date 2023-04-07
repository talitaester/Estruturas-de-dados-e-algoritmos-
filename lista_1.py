class Lista1_EDA:
    def __init__(self):
        pass


    def multiplica(self, x ,y):
        result = 0
        for i in range(x):
            result += y
        return result 
    
    #RESULTADO DA DIVISÃO INTEIRA   
    def divide(self, x, y):
        
        result = 1
        while x > y:
            x -= y
            result += 1
        return result 
    
    def potencia(self, x, y):
        result = 0
        for i in range(y):
            if i == 0:
                result = x
            else:
                result = result*x
        return result 
            
    def primo(self, number):
        result = 0
        if (number == 2) or (number == 3) or (number == 5) or (number == 7):
            result = 1
        elif (number % 2) == 0:
            result = 0
        elif (number % 3) == 0:
            result = 0
        elif (number % 5) == 0:
            result = 0
        elif (number % 7) == 0:
            result = 0
        else:
            result = 1
        return(result)
        
    def fatorial(self, number):
        result = number
        while number > 1:
            number -= 1
            result *= number
            
        return result 

    def inteiros(self, number):
        result = 0
        for i in range(2, number):
            result += i
        return result
    
    def fibonacci(self, number):
        result = 0
        pre_1 = 1
        pre_2 = 0
        result_list = [0, 1]
        for i in range(number-1):
            result = pre_1 + pre_2
            result_list.append(result)
            pre_2 = pre_1
            pre_1 = result

        return result_list[number]
    

    def multiplos(self, number):
        result_list = []
        for i in range(1, number):
            if (i % 3 == 0) or (i % 5 == 0):
                result_list.append(i)
        return result_list
    
    def maior(self, list):
        max = 0
        for i in list:
            if i > max:
                max = i
        return max
    
    def menor(self, list):
        min = list[0]
        for i in list:
            if i <= min:
                min = i
        return min

    def media(self, list):
        sum = 0
        for i in list:
            sum += i
        mean = sum / len(list) 
        return mean 

    def somatriz(self, matrix):
        sum = 0
        for i, j in enumerate(matrix):
            for x, y in enumerate(j):
                sum += y
        return sum
    
    def somacoluna(self, matrix):
        collumm_sum = 0
        for i in matrix[0]:
            collumm_sum += i
        return collumm_sum
    
    def somadiagonal(self, matriz):
        diagonal_sum = 0
        for i, j in enumerate(matriz):
            diagonal_sum += j[i]
        return diagonal_sum
    
    def pertence(self, list1, list2):
        #listas precisam estar set(list) SEM ELEMENTOS REPETIDOS EM NENHUMA DELAS
        intersection = 0
        for i in list1:
            if i in list2:
                intersection += i
        return intersection

    def produtointerno(self, list1, list2):
        sum = 0
        for i in range(len(list1)):
            sum += list1[i] * list2[i]
        return sum
            






    

            
             
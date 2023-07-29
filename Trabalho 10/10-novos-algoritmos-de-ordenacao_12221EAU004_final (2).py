#Giovana Soares Porto
#12221EAU004

#fun principal
def main():
    #recebe lista dos numeros pelo metodo split()
    lista_original=[int(x) for x in input().split()]
    #printa saida final
    print("Algoritmo Seleção e Inserção:")
    algoritmoSI(lista_original)
    print()
    print("Algoritmo Bubble Up and Down:")
    algoritmoBUD(lista_original)


#fun secundaria para o metodo selection insertion
def algoritmoSI(lista_original):
    #cria lista ordenada
    ordenada = [i for i in lista_original]
    ordenada.sort()
    #cria lista para ser printada
    solucao = [i for i in lista_original]
    #variavel que conta num de trocas
    trocas = 0
    #tamanho da subsequencia maximal
    tam_subseq = 2

    #laco que roda enquanto as duas lista nao forem iguais (condicao de parada)
    for i in range (len(solucao)):
        #condicao de parada
        if verifica(ordenada,solucao):
            break

        #encontra o menor valor dentre os que ja nao foram trocados 
        menor_pos = i
        menor = solucao[menor_pos]
        for j in range (tam_subseq-1, len(solucao)):
            if (solucao[j] < solucao[menor_pos]):
                menor_pos = j
                menor = solucao[menor_pos]

        #insere o menor na posicao i e deleta o original
        del(solucao[menor_pos])
        solucao.insert(i,menor)
        tam_subseq += 1
        #soma o num de trocas
        trocas += menor_pos - i

        #se houve mudanca de posicao, printa
        if menor_pos - i > 0:
            print(solucao)

    #printa num de trocas 
    print("Trocas realizadas:",trocas)


#fun secundaria para o metodo bubble up and down
def algoritmoBUD(lista_original):
    #cria lista ordenada
    ordenada = [i for i in lista_original]
    ordenada.sort()
    #cria lista para ser printada
    solucao = [i for i in lista_original]
    #variavel que conta num de trocas
    trocas = 0
    
    #laco que roda enquanto as duas lista nao forem iguais (condicao de parada)
    while True:
        #se as listas nao forem iguais faz o metodo bubble up
        if not verifica(ordenada,solucao):
            for j in range(len(solucao)-1):
                #se o valor lido for maior que seu sucessor, troca eles de lugar
                if (solucao[j] > solucao[j+1]):
                    x = solucao.pop(j)
                    solucao.insert(j+1, x)
                    #soma o num de trocas
                    trocas += 1
            print(solucao)

        #se as listas nao forem iguais faz o metodo bubble down
        if not verifica(ordenada,solucao):
            for j in range(len(solucao)-1):
                #inverte a lista para colocar ela em ordem decrescente
                solucao.reverse()
                #se o valor lido for menor que seu sucessor, troca eles de lugar
                if (solucao[j] < solucao[j+1]):
                    x = solucao.pop(j)
                    solucao.insert(j+1, x)
                    #soma o num de trocas
                    trocas += 1
                #desinverte a lista
                solucao.reverse()
            print(solucao)
        
        #condicao de parada
        if verifica(ordenada,solucao):
            break

    #printa num de trocas  
    print("Trocas realizadas:", trocas)

#funcao secundaria que  verifica se duas lista sao iguais
def verifica(lista1, lista2):
    for i in range(len(lista1)):
        if lista1[i] != lista2[i]:
            return False
    return True

#chama a fun principal
main()
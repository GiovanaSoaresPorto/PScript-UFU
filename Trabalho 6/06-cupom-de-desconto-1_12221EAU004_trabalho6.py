#Giovana Soares Porto 
#12221EAU004

#funcao principal 
def main():
    #entrada das variaveis
    X1 = int(input())
    Z1 = int(input())
    X2 = int(input())
    Z2 = int(input())
    X3 = int(input())
    Z3 = int(input())
    n = int(input())

    #criei uma lista com os valores das n compras 
    lista_compras = [int(input()) for i in range(n)]
    
    #criei uma lista com os descontos do primeiro cupom 
    descontos1 = []
    #percorre cada i da lista de compras
    for i in range(n):
        #se o valor da compra for maior que Z1 recebe X1 de desconto, se n, recebe 0 desconto 
        if lista_compras[i] > Z1:
            descontos1.append(X1)
        else:
            descontos1.append(0)
    
    descontos2 = []
    #percorre cada i da lista de compras
    for i in range(n):
        #recebe um desconto de X2% no valor da compra, com esse desconto maximo ate Z2(quando o desconto for maior que Z2, ele fica igual a Z2)
        desconto = (X2/100) * lista_compras[i]
        if desconto > Z2:
            desconto = Z2
        descontos2.append(desconto)
        
    descontos3 = []
    #percorre cada i da lista de compras
    for i in range(n):
        #se a compra for maior que Z3, recebe X3% de desconto do valor, se for menor recebe 0 
        if lista_compras[i] > Z3:
            descontos3.append(X3/100 * lista_compras[i])
        else:
            descontos3.append(0)

    calculo_desconto(n, descontos1,descontos2,descontos3) #chama a funcao que calcula o desconto total

#funcao secundaria que calcula o desconto total e imprime a melhor combinacao possivel 
def calculo_desconto(n, descontos1,descontos2,descontos3): 
    #os indices dos melhores descontos, iniciam em zero  
    COMPRA_I = 0
    COMPRA_J = 0
    COMPRA_K = 0  
    #desconto total inicia em zero 
    desconto_total = 0
    
    #percorre cada elemento das 3 listas de desconto 
    for i in range(n):
        for j in range(n):
            for k in range(n):
                #combinacao comeca em 0
                combinacao = 0
                #se os indices forem diferentes a combinação recebe o valor da soma dos 3 descontos 
                if i != j and i != k and j != k:
                    combinacao = descontos1[i] + descontos2[j] + descontos3[k]
                    #se a combinacao for maior que o desconto total, essa passa ser a melhor combinaçao 
                    if combinacao > desconto_total:
                        desconto_total = combinacao
                        COMPRA_I = i
                        COMPRA_J = j
                        COMPRA_K = k

    #imprime os indices da melhor combinacao                    
    print("Cupom 1:", COMPRA_I+1)
    print("Cupom 2:", COMPRA_J+1)
    print("Cupom 3:", COMPRA_K+1)

main()
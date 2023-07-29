#Giovana Soares Porto
#1221EAU004

def main(): #funcao principal
    dinheiro= float(input())  #dinheiro que joao possui
    precobooster= float(input()) #preco do booster 
    cartasnovas= int(input())   #quantidade de cartas verdes ou pretas novas que joao quer
    #quantidade de boosters comprados e cartas das cores verde ou preta obtidas inicia em zero
    bcomprados= 0 
    a= 0
    #criei as variaveis resto e numcartas com objetivo de nao mudar as variaveis ja existentes dinheiro e cartas novas durante o programa 
    resto= dinheiro
    numcartas = cartasnovas
    
    while (resto > precobooster): #enquanto joao tiver dinheiro para compra booster
        resto = resto - precobooster #calculo do dinheiro gasto em compra de booster 
        bcomprados = bcomprados + 1 #quantidade de booster comprados
        
        a, numcartas = cartasadquiridas(a, numcartas) #chamar a funcao cartasadquiridas 
        
        if(numcartas == 0): #se joao conseguiu comprar a quantidade de cartas q ele queria, quebra o laco 
            break

 #saidas de acordo com o trabalho   
    print(("ORCAMENTO: {} REAIS").format(dinheiro))
    print(("VALOR DO BOOSTER: {} REAIS").format(precobooster))
    print(("TOTAL GASTO: {:.2f} REAIS").format(precobooster * bcomprados))
    print(("TOTAL RESTANTE: {:.2f} REAIS").format(resto))        
    print(("QUANTIDADE DE BOOSTERS COMPRADOS: {}").format(bcomprados))
    print(("QUANTIDADE DESEJADA DE CARTAS DA COR VERDE OU DA COR PRETA: {}").format(cartasnovas))
    print(("QUANTIDADE OBTIDA DE CARTAS DA COR VERDE OU DA COR PRETA: {}").format(a))

    if(cartasnovas == a):
        print("JOAO CONSEGUIU MONTAR SEU NOVO DECK!")
    else:
        print("JOAO NAO CONSEGUIU MONTAR SEU NOVO DECK!")    

#criei uma funcao que controla o numero de cartas verde ou pretas adquiridas 
def cartasadquiridas(a, numcartas):
    c = int(input()) #entrada das cores das cartas 
    if(c== 5 or c== 3): #se essa carta for verde ou preta 
            numcartas = numcartas -1 #diminuir uma carta que joao queria a cada volta no laco
            a += 1 #quantidades de cartas da cor verde ou preta obtidas
    return a,numcartas 

#chama a funcao main
main()

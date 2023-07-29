#Giovana Soares Porto
#12221EAU004

def main():
    #lista com o numero de jogos e os pesos das medalhas   
    l1=input().split()
    N= int(l1[0])
    ouro=int(l1[1])
    prata=int(l1[2])
    bronze= int(l1[3])

    #dicionario vazio para armazenar os nomes dos paises e suas pontuações  
    paises={}
    #lista vazia para armazenar os jogos que ganharam ouro 
    esportes_ganhos = []

    #laco de i que percorre o numero de jogos
    for i in range(N):
        #lista com o jogo e as respectivas tres posicoes 
        l2= input().split()
        #adicionar o jogo e o pais que ficou em primeiro lugar  
        esportes_ganhos.append([l2[0],l2[1]])
        #se o pais estiver no dicionario, somar a respectiva pontuacao da sua colocacao   
        if l2[1] in paises:
            paises[l2[1]] += ouro 
        if l2[2] in paises:
            paises[l2[2]] += prata   
        if l2[3] in paises:
            paises[l2[3]] += bronze
        #se o pais nao estiver no dicionario, o pais recebe a pontucao da sua colocacao 
        if l2[1] not in paises:
            paises[l2[1]] = ouro
        if l2[2] not in paises:
            paises[l2[2]] = prata 
        if l2[3] not in paises:
            paises[l2[3]]= bronze

    #cria lista com nomes dos paises em ordem alfabetica
    nomes = sorted(list(paises.keys()), key=str)

    # cria lista com pontuacao dos paises na ordem em que aparecem em nomes
    pontuacao =[]
    for i in nomes:
        for j in paises:
            if j == i:
                pontuacao.append(paises.get(j))
    maiorpont(pontuacao, nomes, esportes_ganhos)
    
def maiorpont(pontuacao, nomes, esportes_ganhos):
    #encontra os paises com maior pontuacao e cria um lista de primeiro colocado com eles
    maior = 0
    primeiro = []
    for i in range(len(pontuacao)):
        if pontuacao[i] > maior:
            primeiro = []
            primeiro.append(i)
            maior = pontuacao[i]
        elif pontuacao[i] == maior:
            primeiro.append(i)      
        
    # printa os paises em primeiro lugar, sua pontuacao e os esportes que ganharam
    for i in primeiro:
        print("{} {}".format(nomes[i], maior))
        
        for j in esportes_ganhos:
            if j[1] == nomes[i]:
                print(j[0])
        
main()
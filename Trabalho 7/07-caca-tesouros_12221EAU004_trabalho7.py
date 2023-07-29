#Giovana Soares Porto
#12221EAU004

#funcao principal
def main():
    M= [input().split() for i in range(8)] #criei uma matriz 8X8

    #chamei a funcao que acha os tesouros 
    baus = achar_tesouros(M)
            
    #print de acordo com a quantidade de baus encontrados         
    if (baus==0):
        print("Nenhum bau encontrado.")
    if (baus>0):
        print("{} bau(s) encontrado(s).".format(baus))

#funcao de achar tesouros 
def achar_tesouros(M):
    sensores= int(input())
    alcance= int(input())+1
    soma=0
    #laco de i para a quantidade de sensores 
    for i in range(sensores):
        #recebe a posicao inicial do sensor e tranforma a linha e a coluna para inteiro 
        posicao= input().split() 
        linha= int(posicao[0])
        coluna= int(posicao[1])
        #lacos ate o numero de alcance nas direcoes norte,sul,leste e oeste
        for j in range(alcance):
            #se a linha mais o j for menor ou igual a 7
            if(linha+j <= 7):
                #se na posição linha + j for igual a "x" a soma recebe mais 1
                if(M[linha+j][coluna]=="x"):
                    soma+=1
                    #substitui a posicao por "."
                    M[linha+j][coluna]="."
                #se na posicao for "o" para  
                elif(M[linha+j][coluna]=="o"):
                    break
        for j in range(alcance):
            #se a linha menos o j for maior ou igual a 0
            if(linha-j >= 0):
                #se na posição linha - j for igual a "x" a soma recebe mais 1
                if(M[linha-j][coluna]=="x"):
                    soma+=1
                    #substitui a posicao por "."
                    M[linha-j][coluna]="."
                #se na posicao for "o" para
                elif(M[linha-j][coluna]=="o"):
                    break
        for k in range(alcance):
            #se a coluna +k for menor ou igual a 7
            if(coluna+k <= 7):
                #se na posicao coluna + k for igual a "x" a soma recebe mais 1
                if(M[linha][coluna+k]=="x"):
                    soma+=1
                    #substitui a posicao por "."
                    M[linha][coluna+k]="."
                #se na posicao for "o" para  
                elif(M[linha][coluna+k]=="o"):
                    break
        for k in range(alcance):
            #se a coluna -k for maior ou igual a 0 
            if(coluna-k >= 0):
                #se na posicao coluna - k for igual a "x" a soma recebe mais 1
                if(M[linha][coluna-k]=="x"):
                    soma+=1 
                    #substitui a posicao por "."
                    M[linha][coluna-k]="."
                #se na posicao for "o" para
                elif(M[linha][coluna-k]=="o"):
                    break
    #retorna o valor da soma(quantidade de baus no mapa)
    return(soma)

main()
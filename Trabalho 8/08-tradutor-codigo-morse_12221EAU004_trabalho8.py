#Giovana Soares Porto
#12221EAU004

#funcao principal
def main():
    #criei uma lista com as palavras(que sao separadas por dois espacos)
    lista_palavras = input().split("  ")
    
    #tradução comeca vazia
    traducao = ""
    #criei uma matriz com os codigos e suas respectivas letras no alfabeto 
    codigo = [[".-", "A"], ["-...", "B"], ["-.-.", "C"], ["-..", "D"], [".", "E"], ["..-.", "F"], ["--.", "G"], ["....", "H"], ["..", "I"], [".---", "J"], ["-.-", "K"],
              [".-..", "L"], ["--","M"], ["-.", "N"], ["---", "O"], [".--.", "P"], ["--.-", "Q"], [".-.", "R"], ["...", "S"], ["-", "T"], ["..-", "U"], ["...-", "V"],
              [".--", "W"], ["-..-", "X"], ["-.--", "Y"],["--..", "Z"]]
    
    #laco que percorre cada palavra na lista 
    for palavra in lista_palavras:
        #criei uma lista com as letras de cada palavra 
        lista_letras = palavra.split()
        #laco que percorre cada letra da lista  
        for letra in lista_letras:
            #se tiver asterrisco na letra, chama a função converte_morse_corrompido  
            if "*" in letra:
                traducao += converte_morse_corrompido(letra,codigo)
            #se nao tiver asterrisco, chama a funcao converte codigo morse  
            else:
                traducao += converte_morse(letra,codigo)
        #se a palavra não for a ultima da lista de palavras, traducao recebe um espaço
        if palavra!= lista_palavras[-1]:
            traducao+=" "
    #printa a traducao do codigo
    print(traducao)

#funcao que converte os codigos morse 
def converte_morse(letra, codigo):
    #laco que percorre as letras(linha por linha) do codigo 
   for i in range(len(codigo)):
       #se o codigo for igual a uma letra, retorna a letra do alfabeto(codigo[i][1])
       if codigo[i][0] == letra:
           return codigo[i][1]     
    
#funcao que converte os codigos morses corrompidos 
def converte_morse_corrompido(letra, codigo):
    #exclui o asterisco da letra 
    letra = letra.strip("*")
    
    resposta = ""
    #laco que percorre as letra (linha por linha) do codigo
    for i in range(len(codigo)):
        #se a letra de indice i em morse for maior ou igual a letra desejada, entra no if 
        if len(codigo[i][0])>=len(letra):
            #cria uma variavel com o valor da letra de indice i em morse
            letra_morse = codigo[i][0]
            #faz o fatiamento da letra_morse para que fique do tamanho da letra desejada 
            digito_possivel = letra_morse[0:len(letra)]
            
            #se ambas forem iguais, adiciona a letra de indice i em alfabeto nas possiveis respostas
            if digito_possivel == letra:
                resposta += codigo[i][1]
    #resposta recebe as possiveis letras entre colchetes         
    resposta = "[" + resposta + "]"
    
    #retorna a resposta 
    return(resposta)
      
main()
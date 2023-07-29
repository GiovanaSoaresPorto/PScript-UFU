#Giovana Soares Porto 
#12221EAU004

#entrada das variaveis 
n= int(input()) 
soma= 0 #soma dos acessos inicia em 0
dias= 0 #o numero de dias começa em 0

#laço que acaba quando a soma der maior ou igual a 1000000
while(soma < 1000000):
    a = int(input()) 
    soma += a #soma ele mesmo mais o "a" recebido
    dias += 1 #adiciona um dia a cada volta do laço

#saída do numero de dias 
print(dias) 
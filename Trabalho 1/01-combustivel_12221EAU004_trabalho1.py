#Giovana Soares Porto
#12221EAU004
#entrada das variaveis tempo e velocidade em float
tempo= float(input())
velocidade= float(input())

#calculo da distancia
distancia= tempo*velocidade

#calculo da quantidade de litros  
litros= distancia/ 12

#saida da quantidade de litros
print( "{:.3f}".format(litros))
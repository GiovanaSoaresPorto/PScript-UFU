#Giovana Soares Porto
#1221EAU004

#entrada das variaveis 
distancia=int(input())
diferenca_tempo=int(input())
v_1=float(input())
v_2=float(input())

#calculo do tempo de cada trem 
#calculei o tempo gasto do trem 1 e diminui a sua vantagem de tempo(diferança na saída convertida para horas) em relaçao ao trem 2 
t_1= distancia/v_1 - diferenca_tempo/60
#calculei o tempo gasto do trem 2
t_2= distancia/v_2

 
#se t_1<t_2 printa True e se t_2<=t_1 printa False   
if t_1<t_2:
    print(True)
else:
    print(False)    
#Giovana Soares Porto
#12221EAU004

def main(): #funcaoo pricipal 
    valor_trabalho= int(input())
    dias= int(input())
    #horas extras e trabalhadas inicia em zero 
    horas_trabalhadas = 0
    horas_extras_diarias = 0

    while(dias != 0): #enquanto dias for diferente de zero
        horas_trabalhadas_dia = 0 #horas trabalhadas no dia inicia em zero
        periodo= int(input()) 
        while(periodo != 0): #enquanto periodo for diferente de zero
            inicio= int(input())
            fim= int(input())
            horas_trabalhadas_periodo = fim - inicio #horas trabalhadas por periodo são o fim menos o inicio
            horas_trabalhadas_dia += horas_trabalhadas_periodo #horas trabalhadas dia igual a ela mesmo mais as horas do periodo 
            periodo = periodo -1 #diminui o periodo a cada volta no laco
        horas_trabalhadas += horas_trabalhadas_dia #horas trabalhadas igual a ela mesmo mais horas trabalhadas no dia 
        horas_extras_diarias += conta_horas_extras_diarias(horas_trabalhadas_dia) #chama a funcao do calculo de horas extras diarias 
        dias = dias - 1 #diminui o dia a cada volta no laco 
        
    if (horas_trabalhadas > 44): #se horas totais for maior que 44
        horas_extras_semanais = horas_trabalhadas - 44 #calcula horas extras semanais 
        #analisa se horas extras semanais é menor que a diaria e define horas extras como o maior dos dois 
        if (horas_extras_diarias > horas_extras_semanais):  
            horas_extras = horas_extras_diarias
        else:
            horas_extras = horas_extras_semanais
    else: #se não horas extras é igual a diarias
        horas_extras = horas_extras_diarias
        
    #saidas:
    print(("Horas trabalhadas: {}").format(horas_trabalhadas))
    print(("Horas extras: {}").format(horas_extras))
    valor_devido = (valor_trabalho * horas_trabalhadas) + (valor_trabalho/2 * horas_extras)
    print(("Valor devido: R$ {:.2f}").format(valor_devido))  
 
          
def conta_horas_extras_diarias(horas_trabalhadas_dia): #funcao que calcula horas extras diarias 
    if(horas_trabalhadas_dia > 8 ): #se trabalhar mais de 8 horas no dia retorna o resto
        horas_extras_dia = horas_trabalhadas_dia - 8
        return horas_extras_dia
    else: #se não retorna zero
        return 0


main() #chama funcao main
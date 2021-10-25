#Irvin Vásquez Figueroa
#A01541101
#Objetivo: Calcular el IMC y después otorgar qué vacuna se dará mediante estte dato.
n_paciente = 1
#El contador se inicializa en 0 pues ese será el número de paciente que se atienda
print("Hola! Calcularemos tu IMC para así saber qué vacuna te toca, nos iremos paciente por paciente, oki?")
for x in range (0,5):
    #Se abre ciclo for para que se haga 5 veces
    print ("Paciente #" , n_paciente)
   
    n_paciente = n_paciente+1
     #En cada ciclo, se va pasando de paciente 1 a paciente 2, sumando 1 en cada ciclo.
    peso = float(input("¿Cuánto pesas en kg?"))
    altura = float(input("¿Cuál es tu altura en metros?"))
    #Se piden los datos
    IMC = peso/(altura)**2
    #Se calcula el IMC
    print ("Tu IMC es de:" , IMC, ", por lo tanto...")
    print()
    #Se imprime el IMC
    if (IMC>0 and IMC<=19):
        print("Tu vacuna será de tipo A, yay!")
    elif (IMC>19 and IMC<=25):
        print("Tu vacuna será tipo B, yay!")
    elif (IMC>25 and IMC<=29):
        print ("Tu vacuna será tipo C1, yay!")
    elif (IMC>29 and IMC<=35):
        print("Tu vacuna será tipo C2, yay!")
    else:
        print("Tu vacuna será tipo D, yay!")
    #Se abren condicionales para cada caso del IMC, donde si se cumple con cierto valor, la vacuna asignada será tal.
    #Se imprime el resultado, dependiendo de qué condicional se cumplió
    #En else, la condicional sería si es mayor a 35, pues sería el único escenario restante.

print("Adios! c:")
#Se le despide al paciente c:

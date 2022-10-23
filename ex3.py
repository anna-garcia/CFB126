#exercício 3: Programa pede o raio de um círculo e devolve o valor da sua área.
#Área círculo: piR²
import math
pi=math.pi
#importa a biblioteca math que inclui diversas funções matemáticas. O valor de pi exato se encontra nessa livraria na forma de math.pi, mas você pode definir outros valores para pi como pi=3.14, por exemplo.
r=float(input("Digite o valor do raio:"))
r2=float(r*r)
#r2=float(r**2)
area=float(pi*r2)
print(area)

#https://docs.python.org/2/library/math.html - mais informações sobre a biblioteca math

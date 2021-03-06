# -*- coding: utf-8 -*-
"""projeto_redeTrofica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DFri3vp5cHOYZl-vVRHJfcdqaODI8R8l

- Julia Noriko 
- Murilo Holtz Foltran

# Projeto 02 - Redes Tróficas

## Introdução 

  Nesse projeto, foi definida uma rede trófica com 5 espécies. Nela temos uma espécie produtora (planta), duas espécies herbívoras (Pulgão e a Formiga), duas espécies onívoras (Joaninha e Pássaro). No caso da joaninha e do pássaro, foi considerado que a joaninha se alimenta somente do pulgão e que o pássaro se alimenta da formiga e da joaninha.

  Além disso, foi considerado uma relação de mutualismo entre as formigas e os pulgões, já que o pulgão disponibiliza parte da seiva que ele não consome para que a formiga se alimente e em troca a formiga protege os pulgões de seus predadores.

  A partir das interações entre as espécies, foram estabelecidas por meio de equações utilizando o método de Euler a seguinte modelagem:   

  $$ dPlanta/dt = planta(a - bPulgao - aPlanta/K - eFormiga)  $$
  $$ dPulgao/dt = Pulgao(-d + cPlanta + fFormiga - lJoaninha) $$
  $$ dFormiga/dt = Formiga(-g + hPlanta + iPulgao - nPassaro) $$
  $$ dJoaninha = Joaninha(-j + kPulgao - mPassaro) $$
  $$ dPassaro/dt = Passaro(-o + pFormiga + qJoaninha ) $$
"""

import numpy as np
import matplotlib.pyplot as plt
import math

"""## Implementação da rede trófica.
### Simulações e gráficos resultantes. 

Para iniciar a implementação da rede trófica, foram adicionadas uma espécie por vez, exceto no primeiro caso onde foram utilizadas duas espécies como no Modelo Lotka-Volterra (Presa-Predador). As simulações abaixo apresentam os passos que foram utilizados para adicionar cada uma das espécies na rede e a definição dos parâmetros de a até q, que foram sendo alterados para que aparecesse as curvas de cada espécie. Fizemos alterações nos parâmetros até que encontrassemos um equilíbrio entre as curvas de todas as espécies(Exceto a curva da formiga, apresentou uma população baixa).
"""

dt = 0.01
TMax = 50
K = 200

planta0 = 1
pulgao0 = 0.1

a = 0.6
b = 0.75
c = 1
d = 1

x=0.1
y=0.05

planta = planta0
pulgao = pulgao0

planta_array = [planta]
pulgao_array = [pulgao]

t_array = [0]

for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K + y*math.sin(x*t))*dt
    dPulgao = pulgao*( -d + c*planta)*dt

    planta = planta + dPlanta
    pulgao = pulgao +dPulgao

    planta_array.append(planta)
    pulgao_array.append(pulgao)

    t_array.append(t)


plt.plot(t_array, planta_array) #azul
plt.plot(t_array, pulgao_array) #laranja

plt.title('População - Planta-Pulgão')
plt.show()

dt = 0.01
TMax = 50
K = 200

planta0 = 1
pulgao0 = 0.1
formiga0 = 0.1

a = 0.55
b = 0.8
c = 0.4
d = 0.1
e = 0.4
f = 0.3
g = 0.1
h = 0.2
i = 0.1


x=0.5
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0

planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]

t_array = [0]

for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao)*dt


    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga



    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    t_array.append(t)

plt.plot(t_array, planta_array) #azul
plt.plot(t_array, pulgao_array) #laranja
plt.plot(t_array, formiga_array) #verde
plt.title('População - Planta-Pulgão-Formiga')
plt.show()

dt = 0.01
TMax = 50
K = 200

planta0 = 1
pulgao0 = 0.2
formiga0 = 0.3

a = 0.55
b = 0.8
c = 0.7
d = 1
e = 0.5
f = 0.1
g = 0.5
h = 0.35
i = 0.3


x=0.5
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0

planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]

t_array = [0]

for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao)*dt


    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga



    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    t_array.append(t)

plt.plot(t_array, planta_array) #azul
plt.plot(t_array, pulgao_array) #laranja
plt.plot(t_array, formiga_array) #verde

plt.title('População - Planta-Pulgão-Formiga')
plt.show()

dt = 0.01
TMax = 50
K = 200

planta0 = 1
pulgao0 = 0.3
formiga0 = 0.3
joaninha0 = 0.2

a = 0.55
b = 0.8
c = 0.7
d = 1
e = 0.5
f = 0.1
g = 0.4
h = 0.4
i = 0.3
j = 0.2
k = 0.5
l = 0.1


x=0.5
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0
joaninha = joaninha0

planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]
joaninha_array = [joaninha]

t_array = [0]

for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga - l*joaninha)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao)*dt
    dJoaninha = joaninha*(-j + k*pulgao)*dt

    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga
    joaninha = joaninha + dJoaninha

    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    joaninha_array.append(joaninha)

    t_array.append(t)


plt.plot(t_array, planta_array, label='Planta') #azul
plt.plot(t_array, pulgao_array, label='Pulgão') #laranja
plt.plot(t_array, formiga_array, label='Formiga') #verde
plt.plot(t_array, joaninha_array, label='Joaninha') #vermelho

plt.title('População - Planta-Pulgão-Formiga-Joaninha')
plt.legend()
plt.show()

dt = 0.01
TMax = 50
K = 200

planta0 = 0.5
pulgao0 = 0.1
formiga0 = 0.5
joaninha0 = 0.05
passaro0 = 0.15

a = 0.55
b = 0.8
c = 0.4
d = 0.1
e = 0.5
f = 0.2
g = 0.5
h = 0.35
i = 0.3
j = 0.1
k = 0.3
l = 0.2
m = 0.3
n = 0.2
o = 0.3
p = 0.5
q = 0.6

x=0.5
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0
joaninha = joaninha0
passaro = passaro0

planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]
joaninha_array = [joaninha]
passaro_array = [passaro]
t_array = [0]

for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga - l*joaninha)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao - n*passaro)*dt
    dJoaninha = joaninha*(-j + k*pulgao - m*passaro)*dt
    dPassaro = passaro*(-o + p*formiga + q*joaninha )*dt

    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga
    joaninha = joaninha + dJoaninha
    passaro = passaro + dPassaro

    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    joaninha_array.append(joaninha)
    passaro_array.append(passaro)
    t_array.append(t)


plt.plot(t_array, planta_array, label='Planta') #azul
plt.plot(t_array, pulgao_array, label='Pulgão') #laranja
plt.plot(t_array, formiga_array, label='Formiga') #verde
plt.plot(t_array, joaninha_array, label='Joaninha') #vermelho
plt.plot(t_array, passaro_array, label='Pássaro') #Lilás

plt.title('População - Planta-Pulgão-Formiga-Joaninha-Passaro')
plt.legend()
plt.show()

dt = 0.01
TMax = 50
K = 200

planta0 = 3
pulgao0 = 0.1
formiga0 = 0.2
joaninha0 = 0.05
passaro0 = 0.2
cobra0 = 0.2
a = 0.5
b = 0.8
c = 1
d = 1
e = 0.5
f = 0.2
g = 0.5
h = 0.35
i = 0.3
j = 0.1
k = 0.3
l = 0.2
m = 0.3
n = 0.2
o = 0.3
p = 0.5
q = 0.6
r = 0.1
s = 0.2
t = 0.2

x=0.5
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0
joaninha = joaninha0
passaro = passaro0
cobra = cobra0
planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]
joaninha_array = [joaninha]
passaro_array = [passaro]
cobra_array = [cobra]
t_array = [0]



for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga - l*joaninha)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao -n*passaro)*dt
    dJoaninha = joaninha*(-j + k*pulgao - m*passaro)*dt
    dPassaro = passaro*(-o + p*formiga + q*joaninha - t*cobra)*dt
    dCobra = cobra*(-r + s*passaro)*dt


    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga
    joaninha = joaninha + dJoaninha
    passaro = passaro + dPassaro
    cobra = cobra + dCobra

    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    joaninha_array.append(joaninha)
    passaro_array.append(passaro)
    cobra_array.append(cobra)
    t_array.append(t)


plt.plot(t_array, planta_array, label='Planta') #azul
plt.plot(t_array, pulgao_array, label='Pulgão') #laranja
plt.plot(t_array, formiga_array, label='Formiga') #verde
plt.plot(t_array, joaninha_array, label='Joaninha') #vermelho
plt.plot(t_array, passaro_array, label='Pássaro') #Lilás
plt.plot(t_array, cobra_array) #Marrom

plt.title('População - Planta-Pulgão-Formiga-Joaninha-Passaro-Cobra')
plt.legend()
plt.show()

dt = 0.01
TMax = 50
K = 200

planta0 = 1
pulgao0 = 0.1
formiga0 = 0.2
joaninha0 = 0.05
passaro0 = 0.2
cobra0 = 0.2
a = 0.5
b = 0.8
c = 1
d = 1
e = 0.5
f = 0.2
g = 0.5
h = 0.35
i = 0.3
j = 0.1
k = 0.3
l = 0.2
m = 0.3
n = 0.2
o = 0.3
p = 0.5
q = 0.6
r = 0.1
s = 0.2
t = 0.2

x=0.3
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0
joaninha = joaninha0
passaro = passaro0
cobra = cobra0
planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]
joaninha_array = [joaninha]
passaro_array = [passaro]
cobra_array = [cobra]
t_array = [0]



for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga - l*joaninha)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao -n*passaro)*dt
    dJoaninha = joaninha*(-j + k*pulgao - m*passaro)*dt
    dPassaro = passaro*(-o + p*formiga + q*joaninha - t*cobra)*dt
    dCobra = cobra*(-r + s*passaro)*dt


    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga
    joaninha = joaninha + dJoaninha
    passaro = passaro + dPassaro
    cobra = cobra + dCobra

    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    joaninha_array.append(joaninha)
    passaro_array.append(passaro)
    cobra_array.append(cobra)
    t_array.append(t)

plt.plot(t_array, planta_array, label='Planta') #azul
plt.plot(t_array, pulgao_array, label='Pulgão') #laranja
plt.plot(t_array, formiga_array, label='Formiga') #verde
plt.plot(t_array, joaninha_array, label='Joaninha') #vermelho
plt.plot(t_array, passaro_array, label='Pássaro') #Lilás
plt.plot(t_array, cobra_array, label='Cobra') #Marrom

plt.title('Rede Trófica')
plt.legend()
plt.show()

dt = 0.01
TMax = 50
K = 200

planta0 = 1
pulgao0 = 0.1
formiga0 = 0.2
joaninha0 = 0.05
passaro0 = 0.2
cobra0 = 0.2
a = 0.5
b = 0.8
c = 1
d = 1
e = 0.5
f = 0.2
g = 0.5
h = 0.35
i = 0.3
j = 0.1
k = 0.3
l = 0.2
m = 0.3
n = 0.2
o = 0.3
p = 0.5
q = 0.6
r = 0.1
s = 0.2
t = 0.2

x=0.5
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0
joaninha = joaninha0
passaro = passaro0
cobra = cobra0
planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]
joaninha_array = [joaninha]
passaro_array = [passaro]
cobra_array = [cobra]
t_array = [0]



for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga - l*joaninha)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao -n*passaro)*dt
    dJoaninha = joaninha*(-j + k*pulgao - m*passaro)*dt
    dPassaro = passaro*(-o + p*formiga + q*joaninha - t*cobra)*dt
    dCobra = cobra*(-r + s*passaro)*dt


    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga
    joaninha = joaninha + dJoaninha
    passaro = passaro + dPassaro
    cobra = cobra + dCobra

    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    joaninha_array.append(joaninha)
    passaro_array.append(passaro)
    cobra_array.append(cobra)
    t_array.append(t)

plt.plot(t_array, planta_array, label='Planta') #azul
plt.plot(t_array, pulgao_array, label='Pulgão') #laranja
plt.plot(t_array, formiga_array, label='Formiga') #verde
plt.plot(t_array, joaninha_array, label='Joaninha') #vermelho
plt.plot(t_array, passaro_array, label='Pássaro') #Lilás
plt.plot(t_array, cobra_array, label='Cobra') #Marrom

plt.title('Rede Trófica')
plt.legend()
plt.show()

dt = 0.01
TMax = 50
K = 200

planta0 = 0.9
pulgao0 = 0.1
formiga0 = 0.2
joaninha0 = 0.05
passaro0 = 0.3
cobra0 = 0.4
a = 0.5
b = 0.8
c = 0.9
d = 0.9
e = 0.5
f = 0.2
g = 0.5
h = 0.35
i = 0.3
j = 0.1
k = 0.3
l = 0.2
m = 0.3
n = 0.2
o = 0.3
p = 0.5
q = 0.6
r = 0.1
s = 0.2
t = 0.2

x=0.4
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0
joaninha = joaninha0
passaro = passaro0
cobra = cobra0
planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]
joaninha_array = [joaninha]
passaro_array = [passaro]
cobra_array = [cobra]
t_array = [0]

for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga - l*joaninha)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao -n*passaro)*dt
    dJoaninha = joaninha*(-j + k*pulgao - m*passaro)*dt
    dPassaro = passaro*(-o + p*formiga + q*joaninha - t*cobra)*dt
    dCobra = cobra*(-r + s*passaro)*dt


    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga
    joaninha = joaninha + dJoaninha
    passaro = passaro + dPassaro
    cobra = cobra + dCobra

    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    joaninha_array.append(joaninha)
    passaro_array.append(passaro)
    cobra_array.append(cobra)
    t_array.append(t)

plt.plot(t_array, planta_array, label='Planta') #azul
plt.plot(t_array, pulgao_array, label='Pulgão') #laranja
plt.plot(t_array, formiga_array, label='Formiga') #verde
plt.plot(t_array, joaninha_array, label='Joaninha') #vermelho
plt.plot(t_array, passaro_array, label='Pássaro') #Lilás
plt.plot(t_array, cobra_array, label='Cobra') #Marrom

plt.title('Rede Trófica')
plt.legend()
plt.show()

dt = 0.01
TMax = 100
K = 200

planta0 = 0.9
pulgao0 = 0.1
formiga0 = 0.2
joaninha0 = 0.05
passaro0 = 0.3
cobra0 = 1
a = 0.55
b = 0.8
c = 0.4
d = 0.1
e = 0.5
f = 0.2
g = 0.5
h = 0.35
i = 0.3
j = 0.1
k = 0.7
l = 0.4
m = 0.2
n = 0.1
o = 0.2
p = 0.3
q = 0.2
r = 0.1
s = 0.2
t = 0.1

x=0.4
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0
joaninha = joaninha0
passaro = passaro0
cobra = cobra0
planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]
joaninha_array = [joaninha]
passaro_array = [passaro]
cobra_array = [cobra]
t_array = [0]

for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga - l*joaninha)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao -n*passaro)*dt
    dJoaninha = joaninha*(-j + k*pulgao - m*passaro)*dt
    dPassaro = passaro*(-o + p*formiga + q*joaninha - t*cobra)*dt
    dCobra = cobra*(-r + s*passaro)*dt


    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga
    joaninha = joaninha + dJoaninha
    passaro = passaro + dPassaro
    cobra = cobra + dCobra

    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    joaninha_array.append(joaninha)
    passaro_array.append(passaro)
    cobra_array.append(cobra)
    t_array.append(t)

plt.plot(t_array, planta_array, label='Planta') #azul
plt.plot(t_array, pulgao_array, label='Pulgão') #laranja
plt.plot(t_array, formiga_array, label='Formiga') #verde
plt.plot(t_array, joaninha_array, label='Joaninha') #vermelho
plt.plot(t_array, passaro_array, label='Pássaro') #Lilás
plt.plot(t_array, cobra_array, label='Cobra') #Marrom

plt.title('Rede Trófica')
plt.legend()
plt.show()

"""Como não estávamos conseguindo encontrar parâmetros que permitissem o equilíbrio entre as espécies, já que a curva que descreve a população de cobras não aumentava no decorrer do tempo e mesmo quando iniciava com alto número em sua população ela não apresentava um ciclo de declínio e aumento, apenas entrava em extinção. Então decidimos retirar a cobra para testar e conseguimos os resultados que estão nas simulações abaixo."""

dt = 0.01
TMax = 100
K = 200

planta0 = 0.9
pulgao0 = 0.1
formiga0 = 0.2
joaninha0 = 0.05
passaro0 = 0.3
cobra0 = 0.4
a = 0.55
b = 0.8
c = 0.4
d = 0.1
e = 0.5
f = 0.2
g = 0.5
h = 0.35
i = 0.3
j = 0.1
k = 0.7
l = 0.4
m = 0.2
n = 0.1
o = 0.2
p = 0.3
q = 0.2
r = 0.1
s = 0.2
t = 0.1

x=0.4
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0
joaninha = joaninha0
passaro = passaro0
cobra = cobra0
planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]
joaninha_array = [joaninha]
passaro_array = [passaro]
cobra_array = [cobra]
t_array = [0]

for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga - l*joaninha)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao -n*passaro)*dt
    dJoaninha = joaninha*(-j + k*pulgao - m*passaro)*dt
    dPassaro = passaro*(-o + p*formiga + q*joaninha )*dt
    #- t*cobra
    #dCobra = cobra*(-r + s*passaro)*dt


    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga
    joaninha = joaninha + dJoaninha
    passaro = passaro + dPassaro
    #cobra = cobra + dCobra

    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    joaninha_array.append(joaninha)
    passaro_array.append(passaro)
    #cobra_array.append(cobra)
    t_array.append(t)

plt.plot(t_array, planta_array, label='Planta') #azul
plt.plot(t_array, pulgao_array, label='Pulgão') #laranja
plt.plot(t_array, formiga_array, label='Formiga') #verde
plt.plot(t_array, joaninha_array, label='Joaninha') #vermelho
plt.plot(t_array, passaro_array, label='Pássaro') #Lilás
#plt.plot(t_array, cobra_array, label='Cobra') #Marrom

plt.title('Rede Trófica')
plt.legend()
plt.show()

"""### Simulação cujo o gráfico chegou próximo ao equilíbrio entre as espécies 

> Simulação com os parâmetros que permitem que todas as espécies estejam em equilíbrio. As formigas continuam com população baixa, pois como os pássaros se alimentam delas e eles não possuem um predador diminuindo sua população, as formigas acabam tendo uma drástica diminuição.
"""

dt = 0.01
TMax = 100
K = 200

planta0 = 0.5
pulgao0 = 0.1
formiga0 = 0.5
joaninha0 = 0.05
passaro0 = 0.15
cobra0 = 0.2
a = 0.55
b = 0.8
c = 0.4
d = 0.1
e = 0.5
f = 0.2
g = 0.5
h = 0.35
i = 0.3
j = 0.1
k = 0.7
l = 0.4
m = 0.2
n = 0.1
o = 0.2
p = 0.3
q = 0.2
r = 0.1
s = 0.2
t = 0.1

x=0.5
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0
joaninha = joaninha0
passaro = passaro0
cobra = cobra0
planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]
joaninha_array = [joaninha]
passaro_array = [passaro]
cobra_array = [cobra]
t_array = [0]

for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga - l*joaninha)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao - n*passaro)*dt
    dJoaninha = joaninha*(-j + k*pulgao - m*passaro)*dt
    dPassaro = passaro*(-o + p*formiga + q*joaninha )*dt
    #dCobra = cobra*(-r + s*passaro)*dt - t*cobra

    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga
    joaninha = joaninha + dJoaninha
    passaro = passaro + dPassaro
    #cobra = cobra + dCobra


    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    joaninha_array.append(joaninha)
    passaro_array.append(passaro)
    t_array.append(t)
    cobra_array.append(cobra)


plt.plot(t_array, planta_array, label='Planta') #azul
plt.plot(t_array, pulgao_array, label='Pulgão') #laranja
plt.plot(t_array, formiga_array, label='Formiga') #verde
plt.plot(t_array, joaninha_array, label='Joaninha') #vermelho
plt.plot(t_array, passaro_array, label='Pássaro') #Lilás
#plt.plot(t_array, cobra_array, label='Cobra') #Marrom

plt.title('Rede Trófica')
plt.legend()
plt.show()

"""### Simulação adicionando todas as espécies como planejado
Quando adicionamos a cobra na rede trófica em que havia o equilíbrio entre as espécies. Conseguimos que a população de formigas aumentasse e diminuisse conforme as outras espécies, já que as cobras se alimentam de parte da população de pássaros. Todas as espécies possuem um ciclo, onde há tempos de aumento de população e tempos de diminuição, porém a cobra por estar no topo da cadeia alimentar e possuir apenas uma única presa(pássaro) faz com que sua população não tenha mudanças em ciclos como as demais espécies.
"""

dt = 0.01
TMax = 100
K = 200

planta0 = 0.8
pulgao0 = 0.1
formiga0 = 0.5
joaninha0 = 0.05
passaro0 = 0.15
cobra0 = 0.4
a = 0.55
b = 0.8
c = 0.4
d = 0.1
e = 0.5
f = 0.2
g = 0.5
h = 0.35
i = 0.3
j = 0.1
k = 0.7
l = 0.4
m = 0.4
n = 0.1
o = 0.3
p = 0.3
q = 0.2
r = 0.3
s = 0.5
t = 0.2

x=0.5
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0
joaninha = joaninha0
passaro = passaro0
cobra = cobra0
planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]
joaninha_array = [joaninha]
passaro_array = [passaro]
cobra_array = [cobra]
t_array = [0]

for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga - l*joaninha)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao - n*passaro)*dt
    dJoaninha = joaninha*(-j + k*pulgao - m*passaro)*dt
    dPassaro = passaro*(-o + p*formiga + q*joaninha - t*cobra)*dt
    dCobra = cobra*(-r + s*passaro)*dt 

    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga
    joaninha = joaninha + dJoaninha
    passaro = passaro + dPassaro
    cobra = cobra + dCobra


    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    joaninha_array.append(joaninha)
    passaro_array.append(passaro)
    t_array.append(t)
    cobra_array.append(cobra)


plt.plot(t_array, planta_array, label='Planta') #azul
plt.plot(t_array, pulgao_array, label='Pulgão') #laranja
plt.plot(t_array, formiga_array, label='Formiga') #verde
plt.plot(t_array, joaninha_array, label='Joaninha') #vermelho
plt.plot(t_array, passaro_array, label='Pássaro') #Lilás
plt.plot(t_array, cobra_array, label='Cobra') #Marrom

plt.title('Rede Trófica')
plt.legend()
plt.show()

"""## Simulações considerando perturbações

### Extinção da espécie de pulgões

Como esperado o resultado foi que com a extinção dos pulgões a população de joaninhas que se alimentava exclusivamente deles foi extinta também.
"""

dt = 0.01
TMax = 100
K = 200

planta0 = 0.5
formiga0 = 0.5
joaninha0 = 0.05
passaro0 = 0.15
cobra0 = 0.2
a = 0.55
b = 0.8
c = 0.4
d = 0.1
e = 0.5
f = 0.2
g = 0.5
h = 0.35
i = 0.3
j = 0.1
k = 0.7
l = 0.4
m = 0.2
n = 0.1
o = 0.2
p = 0.3
q = 0.2
r = 0.1
s = 0.2
t = 0.1

x=0.5
y=0.2

planta = planta0
formiga = formiga0
joaninha = joaninha0
passaro = passaro0
#cobra = cobra0

planta_array = [planta]
formiga_array = [formiga]
joaninha_array = [joaninha]
passaro_array = [passaro]
#cobra_array = [cobra]
t_array = [0]

for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dFormiga = formiga*(-g + h*planta - n*passaro)*dt
    dJoaninha = joaninha*(-j - m*passaro)*dt
    dPassaro = passaro*(-o + p*formiga + q*joaninha )*dt
    #dCobra = cobra*(-r + s*passaro)*dt - t*cobra

    planta = planta + dPlanta
    formiga = formiga + dFormiga
    joaninha = joaninha + dJoaninha
    passaro = passaro + dPassaro
    #cobra = cobra + dCobra


    planta_array.append(planta)
    formiga_array.append(formiga)
    joaninha_array.append(joaninha)
    passaro_array.append(passaro)
    t_array.append(t)
    #cobra_array.append(cobra)


plt.plot(t_array, planta_array, label='Planta') #azul
plt.plot(t_array, formiga_array, label='Formiga') #laranja
plt.plot(t_array, joaninha_array, label='Joaninha') #verde
plt.plot(t_array, passaro_array, label='Pássaro') #vermelho
#plt.plot(t_array, cobra_array, label='Cobra') #Marrom

plt.title('Rede Trófica')
plt.legend()
plt.show()

"""### Aumento repentino da vegetação

Com o aumento repentino da vegetação há aumento da população que se alimenta das plantas e isso reflete ainda mais nas próximas espécies, como mostra o gráfico abaixo da simulação. Caso a vegetação não volte a crescer "normalmente" em um período aceitável de tempo, poderá acontecer problemas voltados à falta de espaço e possível efeito contrário de falta de alimento para a população, já que ela aumentou mais do que devia.
"""

dt = 0.01
TMax = 100
K = 200

planta0 = 0.5
pulgao0 = 0.1
formiga0 = 0.5
joaninha0 = 0.05
passaro0 = 0.15
cobra0 = 0.2
a = 0.8
b = 0.8
c = 0.4
d = 0.1
e = 0.5
f = 0.2
g = 0.5
h = 0.35
i = 0.3
j = 0.1
k = 0.7
l = 0.4
m = 0.2
n = 0.1
o = 0.2
p = 0.3
q = 0.2
r = 0.1
s = 0.2
t = 0.1

x=0.5
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0
joaninha = joaninha0
passaro = passaro0
cobra = cobra0
planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]
joaninha_array = [joaninha]
passaro_array = [passaro]
cobra_array = [cobra]
t_array = [0]

for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga - l*joaninha)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao - n*passaro)*dt
    dJoaninha = joaninha*(-j + k*pulgao - m*passaro)*dt
    dPassaro = passaro*(-o + p*formiga + q*joaninha )*dt
    #dCobra = cobra*(-r + s*passaro)*dt - t*cobra

    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga
    joaninha = joaninha + dJoaninha
    passaro = passaro + dPassaro
    #cobra = cobra + dCobra


    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    joaninha_array.append(joaninha)
    passaro_array.append(passaro)
    t_array.append(t)
    cobra_array.append(cobra)


plt.plot(t_array, planta_array, label='Planta') #azul
plt.plot(t_array, pulgao_array, label='Pulgão') #laranja
plt.plot(t_array, formiga_array, label='Formiga') #verde
plt.plot(t_array, joaninha_array, label='Joaninha') #vermelho
plt.plot(t_array, passaro_array, label='Pássaro') #Lilás
#plt.plot(t_array, cobra_array, label='Cobra') #Marrom

plt.title('Rede Trófica')
plt.legend()
plt.show()

"""### Redução repentina da vegetação

Com a redução repentina da vegetação, as espécies herbívoras são as primeiras a sofrer com isso e a última a sentir a redução seria a espécie que está no topo da cadeia alimentar(os pássaros) e se a vegetação não voltar a crescer de forma "normal", poderá levar a extinção de algumas espécies e assim provocar um efeito em cadeia.
"""

dt = 0.01
TMax = 100
K = 200

planta0 = 0.5
pulgao0 = 0.1
formiga0 = 0.5
joaninha0 = 0.05
passaro0 = 0.15
cobra0 = 0.2
a = 0.3
b = 0.8
c = 0.4
d = 0.1
e = 0.5
f = 0.2
g = 0.5
h = 0.35
i = 0.3
j = 0.1
k = 0.7
l = 0.4
m = 0.2
n = 0.1
o = 0.2
p = 0.3
q = 0.2
r = 0.1
s = 0.2
t = 0.1

x=0.5
y=0.2

planta = planta0
pulgao = pulgao0
formiga = formiga0
joaninha = joaninha0
passaro = passaro0
cobra = cobra0
planta_array = [planta]
pulgao_array = [pulgao]
formiga_array = [formiga]
joaninha_array = [joaninha]
passaro_array = [passaro]
cobra_array = [cobra]
t_array = [0]

for t in np.arange(dt, TMax, dt):
    
    dPlanta = planta*( a - b*pulgao - a*planta/K - e*formiga + y*math.sin(x*t))*dt
    dPulgao = pulgao*( - d + c*planta + f*formiga - l*joaninha)*dt
    dFormiga = formiga*(-g + h*planta + i*pulgao - n*passaro)*dt
    dJoaninha = joaninha*(-j + k*pulgao - m*passaro)*dt
    dPassaro = passaro*(-o + p*formiga + q*joaninha )*dt
    #dCobra = cobra*(-r + s*passaro)*dt - t*cobra

    planta = planta + dPlanta
    pulgao = pulgao +dPulgao
    formiga = formiga + dFormiga
    joaninha = joaninha + dJoaninha
    passaro = passaro + dPassaro
    #cobra = cobra + dCobra


    planta_array.append(planta)
    pulgao_array.append(pulgao)
    formiga_array.append(formiga)
    joaninha_array.append(joaninha)
    passaro_array.append(passaro)
    t_array.append(t)
    cobra_array.append(cobra)


plt.plot(t_array, planta_array, label='Planta') #azul
plt.plot(t_array, pulgao_array, label='Pulgão') #laranja
plt.plot(t_array, formiga_array, label='Formiga') #verde
plt.plot(t_array, joaninha_array, label='Joaninha') #vermelho
plt.plot(t_array, passaro_array, label='Pássaro') #Lilás
#plt.plot(t_array, cobra_array, label='Cobra') #Marrom

plt.title('Rede Trófica')
plt.legend()
plt.show()
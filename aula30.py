"""
CONSTANTE = "Variaveis" que não vão mudar durante a execução do programa. Por convenção, são escritas em letras maiúsculas.
Muitas condições no mesmo if (ruim)
   <- contagem de complexidade (ruim)
"""

velocidade = 61 # velocidade de um carro
local_carro = 98 # local em que o carro está na estrada


RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local do radar 1
RADAR_RANGE = 1 # A distancia do radar pega do carro (1km antes e 1km depois do radar)

vel_carro_pass_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1


if vel_carro_pass_radar_1:
    print('velocidade carro passou pelo radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_passou_radar_1 and vel_carro_pass_radar_1:
    print('Carro Multado Pelo Radar 1')

else:
    print('Carro ainda não passou pelo radar 1')
       
    

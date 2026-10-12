vel_car = 81
local_car = 41

VEL_LIMITE = 80
LOCAL_RADAR = 42
RADAR_RANGE = 1

passou_da_vel_permitida = vel_car > VEL_LIMITE
passou_na_vel_permitida = vel_car <= VEL_LIMITE

passou_no_radar = (LOCAL_RADAR - RADAR_RANGE) <= local_car <= (LOCAL_RADAR + RADAR_RANGE)
ainda_nao_passou_radar = local_car < (LOCAL_RADAR - RADAR_RANGE)
ja_passou_radar = local_car > (LOCAL_RADAR + RADAR_RANGE)

if passou_da_vel_permitida:
    print('Voce está acima do limite de velocidade')

if passou_na_vel_permitida:
    print('Sua velocidade é adequada')

if passou_no_radar:
    print('Você está no alcance do radar')

if ainda_nao_passou_radar:
    print('Você ainda não passou pelo radar')

if ja_passou_radar:
    print('Você já passou pelo radar')
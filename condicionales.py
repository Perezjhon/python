#temperature = 20

#if temperature > 35:
    #print('Aviso por alta temperatura')
#else:
    #print('Parámetros normales')

#sentencia if
"""temperature = 48

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
else:
    if temperature < 30:
        print('Nivel naranja')
    else:
        print('Nivel rojo')"""

"""temperature = 9

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
elif temperature < 30:
    print('Nivel naranja')
else:
    print('Nivel rojo') """

#asignaciones de condiciones
"""temperature = 16

if temperature < 30:
    fire_risk = 'LOW'
else:
    fire_risk = 'HIGH'

print(fire_risk)"""
#cortocircuito Logico
"""power = 30
signal_4g = 50

result = power > 25 and signal_4g > 10

print(result)"""

#sentencia Match-case

#Comparando vaores
"""color = '#FF0000'

match color:
    case '#FF0000':
        print('🔴')
    case '#00FF00':
        print('🟢')
    case '#0000FF':
        print('🔵')"""

"""color = '#AF549B'

match color:
    case '#FF0000':
        print('🔴')
    case '#00FF00':
        print('🟢')
    case '#0000FF':
        print('🔵')
    case _:
        print('Unknown color!')"""

#Patrones avanzados

"""point = (3, 7)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')"""
#operador morsa
"""radius = 4.25
if (perimeter := 2 * 3.14 * radius) < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)"""
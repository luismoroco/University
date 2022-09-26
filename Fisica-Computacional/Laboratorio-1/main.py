from methods import FirstEquation, SecondEquation, ThirdEquation
from _types import TypeForMRU, TypeForSecondEq, TypeForThirdEq

# Primera Ecuación

first = FirstEquation()

print(f'(1) Distancia de traslado \n (2) Tiempo \n (3) Velocidad \n')
_action: int = int(input('Elección: '))

if _action == 1:
  _data = TypeForMRU("Velocidad Tiempo")
  first.execute(_data, _action)

if _action == 2:
  _data = TypeForMRU("Velocidad Distancia")
  first.execute(_data, _action)

if _action == 3:
  _data = TypeForMRU("Distancia Tiempo")
  first.execute(_data, _action)

# Segunda Ecuación

second = SecondEquation()

_data = TypeForSecondEq("Velocidad-Cuerpo Tiempo Aceleración")
second.execute(_data)

# Tercera Ecuación

third = ThirdEquation()

_data = TypeForThirdEq("Velocidad-Inicial Tiempo-n Aceleración")
third.execute(_data)
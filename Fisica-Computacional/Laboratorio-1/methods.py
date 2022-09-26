from core import CoreFormulaMethod
from _types import TypeForMRU, TypeForSecondEq, TypeForThirdEq

class FirstEquation(CoreFormulaMethod):  
  def execute(
    self: any,
    data: TypeForMRU, 
    action: int) -> None:
    try:
      """ d = v * t """
      if action == 1: 
        print(f'Objecto Trasladado = {data._x * data._y}')
      if action == 2:
        print(f'Tiempo de traslado = {data._x / data._y}')
      if action == 3:
        print(f'Velocidad = {data._x / data._y}')

    except:
      print(f'Error in First')

class SecondEquation(CoreFormulaMethod):
  def execute(
    self: any, 
    data: TypeForSecondEq) -> None:
    try: 
      """ V0 * t + (1/2 * a * t_{2} """
      res: any = (data._vc * data._t) + ((data._a * ((data._t ** 2)))/2)
      print(f'Objeto trasladado: {res}')

    except:
      print(f'Error in Second')

class ThirdEquation(CoreFormulaMethod):
  def execute(
    self: any,
    data: TypeForThirdEq) -> None:
    try:
      """ V0 + (a * t) """
      res: any = data._vi + (data._a * data._t)
      print(f'Velocidad de: {res}') 

    except:
      print(f'Error i third')

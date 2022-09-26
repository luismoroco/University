""" 
    Types for Data Input
"""

class TypeForMRU:
  _x: float
  _y: float 

  def __init__(
    self, 
    labels: str) -> None:
      try: 
        names = labels.split(' ')
        self._x = float(input(f'{names[0]}: '))
        self._y = float(input(f'{names[1]}: '))

      except:
        print(f'Error in TypeMRU')


class TypeForSecondEq:
  _vc: float
  _t: float
  _a: float

  def __init__(
    self, 
    labels: str) -> None:
      try: 
        names = labels.split(' ')
        self._vc = float(input(f'{names[0]}: '))
        self._t = float(input(f'{names[1]}: '))
        self._a = float(input(f'{names[2]}: '))

      except:
        print(f'Error in TypeSecond')


class TypeForThirdEq:
  _vi: float
  _t: float
  _a: float

  def __init__(
    self,
    labels: str) -> None:
      try:
        names = labels.split(' ')
        self._vi = float(input(f'{names[0]}: '))
        self._t = float(input(f'{names[1]}: '))
        self._a = float(input(f'{names[2]}: '))

      except:
        print(f'Error in TypeThird')    
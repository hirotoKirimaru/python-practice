# -*- coding: utf-8 -*-

from enum import Enum, unique

class Color1(Enum):
    RED = 1 
    BLACK = 2
    WHITE = 2

class Color2(Enum):
    RED = (1, 1)
    BLACK = (2, 2)
    WHITE = (3, 2)

    def __init__(self, id, value):
        self.id = id      
        self._value_ = value

# @uniqueを付けたら重複を許さない
# @unique
class Color3(Enum):
    RED = (1, 1)
    BLACK = (2, 2)
    WHITE = (3, 2)

    def __init__(self, id, value):
        self.id = id      
        self._value_ = value

    # def __new__(cls, id, value):
    #     obj = object.__new__(cls)
    #     obj.id = id
    #     obj._value_ = value
    #     return obj
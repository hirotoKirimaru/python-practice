#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.domain.Color import Color1, Color2

def test_foo():
    count = 1
    for element in Color1:    
        assert element.value == count
        count = count + 1

def test_bar():
    for name, element in Color2.__members__.items():  
        print("***")
        print(name)
        print(element)
        # ***
        # RED
        # Color2.RED
        # ***
        # BLACK
        # Color2.BLACK
        # ***
        # WHITE
        # Color2.BLACK
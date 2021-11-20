#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.domain.fizzBuzz import FizzBuzz

def test_num1():
    actual = FizzBuzz().execute(1)
    assert actual == 1

def test_num2():
    actual = FizzBuzz().execute(2)
    assert actual == 2

def test_num3():
    actual = FizzBuzz().execute(3)
    assert actual == "Fizz"

def test_num6():
    actual = FizzBuzz().execute(6)
    assert actual == "Fizz"

def test_num10():
    actual = FizzBuzz().execute(10)
    assert actual == "Buzz"

def test_num15():
    actual = FizzBuzz().execute(15)
    assert actual == "FizzBuzz"
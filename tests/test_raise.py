#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest

def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        raise ValueError("Exception 123 raised")

def test_excinfo():
    with pytest.raises(RuntimeError) as excinfo:
        raise RuntimeError("ERROR")
    assert str(excinfo.value) == "ERROR"
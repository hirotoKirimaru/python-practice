#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def aiueo():
    return "hiragana"


@pytest.fixture
def kakikukeko():
    return 12345


def test_foo(aiueo, kakikukeko):
    '''fixtureを使うと DIができる'''
    print(aiueo)
    print(kakikukeko)
    assert aiueo == "hiragana"
    assert kakikukeko == 12345

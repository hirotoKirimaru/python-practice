#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def aiueo():
    return "hiragana"


@pytest.fixture
def kakikukeko():
    return 12345


"""fixtureを使うと DIができる"""


def test_foo(aiueo, kakikukeko):
    print(aiueo)
    print(kakikukeko)
    assert aiueo == "hiragana"
    assert kakikukeko == 12345

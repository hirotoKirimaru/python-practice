#!/usr/bin/python
# -*- coding: utf-8 -*-


def test_normal():
    dict = {"a": "a", "b": "b", "c": None}
    all_key_has_value = {k: v for k, v in dict.items() if v is not None}

    print(dict)
    print(all_key_has_value)
    assert dict == {"a": "a", "b": "b", "c": None}
    assert all_key_has_value == {"a": "a", "b": "b"}


class DictDomain:
    @staticmethod
    def action(a: str = "1", b: str = "2", c: str = "3"):
        print(a, b, c)

def test_param_method():
    dict = {"a": "a", "b": "b", "c": None}
    all_key_has_value = {k: v for k, v in dict.items() if v is not None}

    print("11111111111111")
    # THEN
    DictDomain.action(**dict)
    DictDomain.action(**all_key_has_value)
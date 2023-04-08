#!/usr/bin/python
# -*- coding: utf-8 -*-


def test_normal():
    dict = {"a": "a", "b": "b", "c": None}
    all_key_has_value = {k: v for k, v in dict.items() if v is not None}

    print(dict)
    print(all_key_has_value)
    assert dict == {"a": "a", "b": "b", "c": None}
    assert all_key_has_value == {"a": "a", "b": "b"}

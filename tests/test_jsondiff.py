#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
JSONを比較するためのテスト

https://github.com/xlwings/jsondiff
"""
import jsondiff as jd
import pytest
from jsondiff import diff


@pytest.mark.skip(reason="GitHubと同じかどうかの念のため確認")
def test_github():
    """

    https://github.com/xlwings/jsondiff
    """
    print(diff({"a": 1, "b": 2}, {"b": 3, "c": 4}))
    # {'c': 4, 'b': 3, delete: ['a']}

    print(diff(["a", "b", "c"], ["a", "b", "c", "d"]))
    # {insert: [(3, 'd')]}

    print(diff(["a", "b", "c"], ["a", "c"]))
    # {delete: [1]}

    # Typical diff looks like what you'd expect...
    print(diff({"a": [0, {"b": 4}, 1]}, {"a": [0, {"b": 5}, 1]}))
    # {'a': {1: {'b': 5}}}

    # ...but similarity is taken into account
    print(diff({"a": [0, {"b": 4}, 1]}, {"a": [0, {"c": 5}, 1]}))
    # {'a': {insert: [(1, {'c': 5})], delete: [1]}}

    # Support for various diff syntaxes
    print(diff({"a": 1, "b": 2}, {"b": 3, "c": 4}, syntax="explicit"))
    # {insert: {'c': 4}, update: {'b': 3}, delete: ['a']}

    print(diff({"a": 1, "b": 2}, {"b": 3, "c": 4}, syntax="symmetric"))
    # {insert: {'c': 4}, 'b': [2, 3], delete: {'a': 1}}

    # Special handling of sets
    print(diff({"a", "b", "c"}, {"a", "c", "d"}))
    # {discard: set(['b']), add: set(['d'])}

    # Load and dump JSON
    print(diff('["a", "b", "c"]', '["a", "c", "d"]', load=True, dump=True))
    # {"$delete": [1], "$insert": [[2, "d"]]}

    # NOTE: Default keys in the result are objects, not strings!
    d = diff({"a": 1, "delete": 2}, {"b": 3, "delete": 4})
    print(d)
    # {'delete': 4, 'b': 3, delete: ['a']}
    print(d[jd.delete])
    # ['a']
    print(d["delete"])
    # 4
    # Alternatively, you can use marshal=True to get back strings with a leading $
    print(diff({"a": 1, "delete": 2}, {"b": 3, "delete": 4}, marshal=True))
    # {'delete': 4, 'b': 3, '$delete': ['a']}

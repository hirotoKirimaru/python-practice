#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
JSONを比較するためのテスト

https://github.com/xlwings/jsondiff
"""
import json

import jsondiff as jd
import pytest
from jsondiff import diff


def test_if_key_order_diff_then_true():
    """
    キーの順番が異なっても正常とする
    """
    json_data_1 = '{"name": "John", "age": 30, "city": "New York"}'
    json_data_2 = '{"city": "New York", "name": "John", "age": 30}'
    dict_1 = json.loads(json_data_1)
    dict_2 = json.loads(json_data_2)

    # THEN
    actual = jd.diff(dict_1, dict_2)

    assert not actual == True
    # print(actual)

def test_if_value_type_ignore_then_false():
    """
    型が違う場合は異常とする.
    stringの30とintの30.
    """
    json_data_1 = '{"name": "John", "age": 30, "city": "New York"}'
    json_data_2 = '{"city": "New York", "name": "John", "age": "30"}'
    dict_1 = json.loads(json_data_1)
    dict_2 = json.loads(json_data_2)

    # THEN
    actual = jd.diff(dict_1, dict_2)

    assert not actual == False
    # print(actual)

@pytest.mark.skip(reason="ignoreない")
def test_():
    json_data_1 = '''
{
"name": "John",
"age": 30,
"city": "New York",
"updatetime": "2022-04-10T15:30:00Z"
}
'''

    json_data_2 = '''
{
"name": "John",
"age": 30,
"city": "New York",
"updatetime": "2022-04-11T08:00:00Z"
}
'''
    dict_1 = json.loads(json_data_1)
    dict_2 = json.loads(json_data_2)

    actual = jd.diff(dict_1, dict_2, ignore=["updatetime"])
    assert not actual == True
    print(actual)





def test_02():
    json_data_1 = '{"name": "John", "age": 30, "city": "New York"}'
    json_data_2 = '{"name": "Jane", "age": 25, "city": "Los Angeles"}'
    dict_1 = json.loads(json_data_1)
    dict_2 = json.loads(json_data_2)

    diff = jd.diff(dict_1, dict_2)

    if not diff:
        print("JSONデータは同じです。")
    else:
        print("JSONデータは異なります。")
    print(diff)


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

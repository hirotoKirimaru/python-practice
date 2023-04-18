#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
JSONを比較するためのテスト

https://github.com/seperman/deepdiff
"""
import json

import pytest
from deepdiff import DeepDiff


def test_if_key_order_diff_then_true():
    """
    キーの順番が異なっても正常とする
    """
    json_data_1 = '{"name": "John", "age": 30, "city": "New York"}'
    json_data_2 = '{"city": "New York", "name": "John", "age": 30}'
    dict_1 = json.loads(json_data_1)
    dict_2 = json.loads(json_data_2)

    # THEN
    actual = DeepDiff(dict_1, dict_2)

    assert actual == {}
    print(actual)


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
    actual = DeepDiff(dict_1, dict_2)

    assert not actual == {}
    print(actual)


@pytest.mark.skip(reason="オプションが正しくない？")
def test_if_value_type_ignore_but_has_option_then_true():
    """
    型が違う場合は異常とする.
    stringの30とintの30.
    """
    json_data_1 = '{"name": "John", "age": 30, "city": "New York"}'
    json_data_2 = '{"city": "New York", "name": "John", "age": "30"}'
    dict_1 = json.loads(json_data_1)
    dict_2 = json.loads(json_data_2)

    # THEN
    actual = DeepDiff(dict_1, dict_2, ignore_string_type_changes=True)

    assert actual == {}
    print(actual)


def test_if_ignore_column_has_diff_then_True():
    json_data_1 = """
{
"name": "John",
"age": 30,
"city": "New York",
"updatetime": "2022-04-10T15:30:00Z"
}
"""

    json_data_2 = """
{
"name": "John",
"age": 30,
"city": "New York",
"updatetime": "2022-04-11T08:00:00Z"
}
"""
    dict_1 = json.loads(json_data_1)
    dict_2 = json.loads(json_data_2)

    # 一回、Dict型にする必要がある
    actual = DeepDiff(dict_1, dict_2, ignore_order=True, exclude_paths=["updatetime"])

    assert actual == {}
    print(actual)


def test_if_list_column_has_diff_order_then_False_but_option_had_True():
    json_data_1 = """
{
"children": ["John", "Bob", "Cathie"]
}
"""

    json_data_2 = """
{
"children": ["Cathie","John", "Bob"]
}
"""
    dict_1 = json.loads(json_data_1)
    dict_2 = json.loads(json_data_2)

    actual = DeepDiff(dict_1, dict_2)

    assert actual != {}
    print(actual)

    actual2 = DeepDiff(dict_1, dict_2, ignore_order=True)
    assert actual2 == {}
    print(actual2)

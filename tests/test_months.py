#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest

import datetime 
import calendar

now = datetime.datetime(2020, 2, 15, 20, 29, 39)

# 今月の1日
def test_now_month():
    assert now.replace(day=1) == datetime.datetime(2020,2,1,20,29,39)

# 先月の1日
def test_last_month():
    last_month = (now.replace(day=1) - datetime.timedelta(days=1)).replace(day=1)
    assert last_month == datetime.datetime(2020,1,1,20,29,39)

# 来月の1日
def test_next_month():
    max_day = calendar.monthrange(now.year, now.month)[1]
    next_month = now.replace(day=max_day) + datetime.timedelta(days=1)

    assert next_month == datetime.datetime(2020,3,1,20,29,39)

# N月はY日
@pytest.mark.parametrize('month,ans', [
    (1, 31),
    (2, 28),
    (3, 31),
    (4, 30),
    (5, 31),
    (6, 30),
    (7, 31),
    (8, 31),
    (9, 30),
    (10, 31),
    (11, 30),
    (12, 31)
])
def test_end_date(month, ans):
    assert calendar.monthrange(2021, month)[1] == ans

# うるう年
def test_uruu():
    assert calendar.monthrange(2020, 2)[1] == 29



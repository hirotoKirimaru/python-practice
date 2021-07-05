#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime 
import calendar

now = datetime.datetime(2020, 2, 15, 20, 29, 39)

# 今月の1日
def test_now_month():
    assert now.replace(day=1) == datetime.datetime(2020,2,1,20,29,39)

# 先月の1日
def test_last_month():
    assert (now.replace(day=1) - datetime.timedelta(days=1)).replace(day=1) == datetime.datetime(2020,1,1,20,29,39)

# 来月の1日
def test_next_month():
    max_day = calendar.monthrange(now.year, now.month)[1]
    next_month = now.replace(day=max_day) + datetime.timedelta(days=1)

    assert next_month == datetime.datetime(2020,3,1,20,29,39)





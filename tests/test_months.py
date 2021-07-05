#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime 

# 今月の1日
def test_datetime():
    now = datetime.datetime(2020, 2, 15, 20, 29, 39)
    assert now.replace(day=1) == datetime.datetime(2020,2,1,20,29,39)

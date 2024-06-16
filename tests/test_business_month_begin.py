# -*- coding: utf-8 -*-

import pandas as pd
import holidays
from pandas.tseries.offsets import CBMonthBegin, CDay
import pytest


@pytest.mark.parametrize(
    "year, month, expected",
    [
        (2024, 1, "2024-01-03"),
        (2024, 2, "2024-02-02"),
        (2024, 6, "2024-06-04"),
    ]
)
def test_second_business_date(year, month, expected):
    """
    第二営業日 を求める
    """
    # 日本の祝日リストを取得(元旦
    jpholidays = holidays.Japan(years=[year])

    # 日本のカスタムビジネスデー (休日は日本の祝日)
    add_b_day = 2 - 1
    b_day = CDay(n=add_b_day, weekmask="Mon Tue Wed Thu Fri",
                 holidays=jpholidays)

    b_month_begin = CBMonthBegin(weekmask=b_day.weekmask,
                                 holidays=b_day.holidays)

    base = pd.Timestamp(year, month, 1)
    b_base = b_month_begin.rollforward(base)
    assert b_base + b_day == pd.Timestamp(expected)


@pytest.mark.parametrize(
    "year, month, expected",
    [
        (2024, 5, "2024-05-16"),
        (2024, 6, "2024-06-14"),
    ]
)
def test_ten_business_date(year, month, expected):
    """
    第十営業日 を求める
    """
    # 日本の祝日リストを取得(元旦
    jpholidays = holidays.Japan(years=[year])

    # 日本のカスタムビジネスデー (休日は日本の祝日)
    add_b_day = 10 - 1
    b_day = CDay(n=add_b_day, weekmask="Mon Tue Wed Thu Fri",
                 holidays=jpholidays)

    b_month_begin = CBMonthBegin(weekmask=b_day.weekmask,
                                 holidays=b_day.holidays)

    base = pd.Timestamp(year, month, 1)
    b_base = b_month_begin.rollforward(base)
    assert b_base + b_day == pd.Timestamp(expected)

@pytest.mark.parametrize(
    "year, month, date, expected",
    [
        (2024, 5, 2, "2024-05-20"), # 通常営業日
        (2024, 5, 3, "2024-05-20"), # 3日は祝日
    ]
)
def test_add_ten_business_date_ignore_base(year, month, date, expected):
    """
    第十営業日 を加算したときを求める
    (当日を含まない)
    """
    # 日本の祝日リストを取得(元旦
    jp_holidays = holidays.Japan(years=[year])

    # 日本のカスタムビジネスデー (休日は日本の祝日)
    add_b_day = 10
    b_day = CDay(n=add_b_day, weekmask="Mon Tue Wed Thu Fri",
                 holidays=jp_holidays
                 )
    base = pd.Timestamp(year, month, date)
    assert base + b_day == pd.Timestamp(expected)

@pytest.mark.parametrize(
    "year, month, date, expected",
    [
        (2024, 5, 2, "2024-05-17"), # 通常営業日
        (2024, 5, 3, "2024-05-20"), # 3日は祝日
    ]
)
def test_add_ten_business_date_include_base(year, month, date, expected):
    """
    第十営業日 を加算したときを求める
    (当日を含む)
    """
    base = pd.Timestamp(year, month, date)
    # 日本の祝日リストを取得(元旦
    jp_holidays = holidays.Japan(years=[year])

    # 日本のカスタムビジネスデー (休日は日本の祝日)
    base_is_holiday = base in jp_holidays
    add_b_day = 10 - (0 if base_is_holiday else 1)
    b_day = CDay(n=add_b_day, weekmask="Mon Tue Wed Thu Fri",
                 holidays=jp_holidays
                 )
    assert base + b_day == pd.Timestamp(expected)



@pytest.mark.parametrize(
    "year, month, date, expected",
    [
        (2024, 5, 2, "2024-05-16"), # 通常営業日
        (2024, 5, 3, "2024-05-17"), # 3日は祝日
    ]
)
def test_add_ten_business_date_not_japan(year, month, date, expected):
    """
    日本関係なく、第十営業日 を加算したときの求める
    """
    add_b_day = 10
    b_day = CDay(n=add_b_day, weekmask="Mon Tue Wed Thu Fri")
    base = pd.Timestamp(year, month, date)
    assert base + b_day == pd.Timestamp(expected)
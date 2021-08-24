
#!/usr/bin/python
# -*- coding: utf-8 -*-


'''

Flakyなテストレポートは作成しない
 pytest -s e2e.pyt --no-flaky-report



Flakyしない実行：
 pytest -s e2e.py -p no:flaky
'''

from typing import AsyncContextManager
from flaky import flaky
import random

@flaky(max_runs=3)
def test_1():
    '''
    3回実行しなおす
    '''

    assert 1 == random.choice([1, 2, 3])

@flaky(max_runs=4, min_passes=2)
def test_2():
    '''
    4回中、2回以上成功する必要あり
    '''
    assert 1 == random.choice([1, 2])

import time

def delay_rerun(*args):
    print(f"delay_rerun")
    time.sleep(1)
    return True

@flaky(rerun_filter=delay_rerun)
def test_something_else():
    assert 1 == random.choice([1, 2, 3])
    



def is_not_crash(err, *args):
    return not issubclass(err[0], RuntimeError)


@flaky
def test_something():
    '''
    rerun_filterを設定していないので、特定のエラーが出ても何度も実行する
    '''
    print("***************実行*************")
    raise RuntimeError

@flaky(rerun_filter=is_not_crash)
def test_something_else():
    '''
    rerun_filterでRuntimeErrorが起きたら致命的なエラーとして扱うので、
    retryが実行されない
    '''
    print("***************実行*************")
    raise RuntimeError
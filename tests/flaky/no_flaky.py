
#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
# デフォルト値で強制flaky
pytest -s no_flaky.py --force-flaky 

# 細かい設定値を追加する(コードに書いてあるものは上書きしない模様)
pytest -s no_flaky.py --force-flaky --max-runs=4 --min-passes=2


Flakyしない実行：
 pytest -s e2e.py -p no:flaky
'''

import random

def test_1():
    '''
    4回中、2回以上成功する必要あり
    '''
    assert 1 == random.choice([1, 2])



#!/usr/bin/python
# -*- coding: utf-8 -*-

from flaky import flaky
import random

@flaky(max_runs=3)
def test_1():
    assert 1 == random.choice([1, 2, 3])
    # assert 1 == 2
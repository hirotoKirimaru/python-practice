#!/usr/bin/python
# -*- coding: utf-8 -*-



def test_foo():
    datum = ["A", "A", "B", "C"]

    print("***********")
    print(datum)
    print([data for data in datum])
    print(set([data for data in datum]))
    print({data for data in datum})
    print({"A", "A", "B", "C"})

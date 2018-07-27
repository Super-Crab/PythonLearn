#!/usr/bin/python
#coding:utf-8

from __future__ import print_function


def test():
    for x in range(10):
        for y in range(1, x + 1):
            print(str(y) + ' * ' + str(x) + ' = ' + str(y * x) + '\t',end=' ')
        print()

if __name__ == '__main__':
    test()

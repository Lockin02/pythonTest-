#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/15 15:14
# @Author  : Lockin
# @Site    : 
# @File    : use_hashlib.py.py
# @Software: PyCharm

import hashlib

db = {}


def get_md5(contain):
    md5 = hashlib.md5()
    md5.update(contain.encode('utf-8'))
    return md5.hexdigest()


def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
    print(db[username])

def login(username, password):
    if not username in db:
        raise KeyError('username not in db')
    if db[username] == get_md5(password + username + 'the-Salt'):
        return True

if __name__ == '__main__':
    register('47', '123456')
    assert login('47', '123456') == True,'Flase'
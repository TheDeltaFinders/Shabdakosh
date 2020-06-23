#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2020-06-10 13:16


import shabdakosh as sk

def test_db_creation():
    ENGINE, SESSION = sk.db.create_connection(sk.settings.DATABASE)
    sk.db.reset(ENGINE)


if __name__ == '__main__':
    test_db_creation()

#!/usr/bin/python

import urllib2


def is_on():
    try:
        response = urllib2.urlopen('http://www.google.com/', timeout=5)
        return True
    except Exception as ex:
        print(ex)
        return False
